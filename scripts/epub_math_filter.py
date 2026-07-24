#!/usr/bin/env python3
"""Pandoc JSON filter: render display math to self-contained SVG via MathJax.

Inline math is left alone (pandoc's default MathML works well for short
expressions and reflows); display equations become SVG so long equations
scale to the reader's screen width instead of overflowing or vanishing.

Usage: pandoc ... --filter scripts/epub_math_filter.py
"""
import json
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def walk_collect(node, jobs):
    if isinstance(node, dict):
        if node.get('t') == 'Math' and node['c'][0]['t'] == 'DisplayMath':
            jobs.append(node['c'][1])
        else:
            for v in node.values():
                walk_collect(v, jobs)
    elif isinstance(node, list):
        for v in node:
            walk_collect(v, jobs)


def walk_replace(node, svgs, counter):
    if isinstance(node, dict):
        if node.get('t') == 'Math' and node['c'][0]['t'] == 'DisplayMath':
            i = counter[0]
            counter[0] += 1
            svg = svgs.get(str(i))
            if svg is not None:
                return {'t': 'RawInline', 'c': ['html', svg]}
            return node  # renderer failed: keep MathML for this one
        return {k: walk_replace(v, svgs, counter) for k, v in node.items()}
    if isinstance(node, list):
        return [walk_replace(v, svgs, counter) for v in node]
    return node


def main():
    ast = json.load(sys.stdin)

    jobs = []
    walk_collect(ast['blocks'], jobs)
    payload = [{'id': str(i), 'tex': tex, 'display': True}
               for i, tex in enumerate(jobs)]

    proc = subprocess.run(
        ['node', os.path.join(SCRIPT_DIR, 'tex2svg_batch.js')],
        input=json.dumps(payload).encode(),
        capture_output=True,
    )
    sys.stderr.write(proc.stderr.decode())
    if proc.returncode != 0:
        sys.stderr.write('tex2svg_batch.js failed; leaving math as-is\n')
        json.dump(ast, sys.stdout)
        return
    svgs = json.loads(proc.stdout.decode())

    counter = [0]
    ast['blocks'] = walk_replace(ast['blocks'], svgs, counter)
    json.dump(ast, sys.stdout)


if __name__ == '__main__':
    main()
