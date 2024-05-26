#!/usr/bin/env python3
import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Math) and elem.format == 'DisplayMath':
        # Ensure multi-line equations are correctly handled
        if '\\begin' in elem.text and '\\end' in elem.text:
            elem.text = elem.text.replace('\\begin{equation*}', '\\[').replace('\\end{equation*}', '\\]')
            elem.text = elem.text.replace('\\begin{align*}', '\\[').replace('\\end{align*}', '\\]')
            elem.text = elem.text.replace('\\begin{aligned}', '\\begin{array}{l}').replace('\\end{aligned}', '\\end{array}')
    return elem

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
