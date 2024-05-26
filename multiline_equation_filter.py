#!/usr/bin/env python3
import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Math) and elem.format == 'DisplayMath':
        # Example transformation: wrap multi-line equations in \[...\]
        elem.text = f"\\[\n{elem.text}\n\\]"
    return elem

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
