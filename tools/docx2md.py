"""Word (.docx) to Markdown for the site's article pages, faithful to the text.

Paragraphs fully in bold with no closing full stop become headings; bold and italic
runs, links and tables are kept; a line break inside a paragraph starts a new paragraph.

Needs python-docx. To see what a file turns into:
    python3 docx2md.py "file.docx"
"""
import sys, re
import docx
from docx.oxml.ns import qn

def flags(r):
    rpr = r.find(qn('w:rPr')); b = i = False
    if rpr is not None:
        for tag in ('w:b', 'w:i'):
            e = rpr.find(qn(tag))
            if e is not None and e.get(qn('w:val')) not in ('0', 'false'):
                if tag == 'w:b': b = True
                else: i = True
    return b, i

def segments(p, d):
    cur = []
    def run_pieces(r, url=None):
        nonlocal cur
        b, i = flags(r)
        for ch in r.iterchildren():
            if ch.tag == qn('w:t'): cur.append([ch.text or '', b, i, url])
            elif ch.tag == qn('w:tab'): cur.append([' ', b, i, url])
            elif ch.tag in (qn('w:br'), qn('w:cr')):
                yield cur; cur = []
    for el in p._p.iterchildren():
        if el.tag == qn('w:r'):
            yield from run_pieces(el)
        elif el.tag == qn('w:hyperlink'):
            rid = el.get(qn('r:id'))
            url = d.part.rels[rid].target_ref if rid else '#' + (el.get(qn('w:anchor')) or '')
            for r in el.iter(qn('w:r')):
                yield from run_pieces(r, url)
    yield cur

def merge(pieces):
    out = []
    for t, b, i, u in pieces:
        if not t: continue
        if out and out[-1][1:] == [b, i, u]: out[-1][0] += t
        else: out.append([t, b, i, u])
    return out

def wrap(t, mark):
    lead, core, trail = re.match(r'^(\s*)(.*?)(\s*)$', t, re.S).groups()
    return f'{lead}{mark}{core}{mark}{trail}' if core else t

def render(pieces):
    s = ''
    for t, b, i, u in pieces:
        x = t
        if i: x = wrap(x, '*')
        if b: x = wrap(x, '**')
        if u: x = f'[{x}]({u})'
        s += x
    return s.strip()

def para_blocks(p, d, style):
    blocks = []
    for seg in segments(p, d):
        pcs = merge(seg)
        text = ''.join(t for t, *_ in pcs).strip()
        if not text: continue
        all_bold = all(b for t, b, i, u in pcs if t.strip())
        heading = style.startswith('Heading') or style == 'Title' or (all_bold and not text.endswith('.') and len(text) < 120)
        blocks.append(('h', text) if heading and not any(u for *_, u in pcs) else ('p', render(pcs)))
    return blocks

def table_md(t):
    rows = [[re.sub(r'\s+', ' ', c.text.strip().replace('|', '\\|')) for c in r.cells] for r in t.rows]
    lines = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * len(rows[0])]
    lines += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
    return '\n'.join(lines)

def convert(path):
    d = docx.Document(path); blocks = []
    for el in d.element.body.iterchildren():
        if el.tag == qn('w:p'):
            p = docx.text.paragraph.Paragraph(el, d)
            blocks += para_blocks(p, d, p.style.name if p.style is not None else '')
        elif el.tag == qn('w:tbl'):
            blocks.append(('t', table_md(docx.table.Table(el, d))))
    return blocks

EMAIL = 'dorithkleinstein@gmail.com'
def yq(s): return "'" + s.replace("'", "''") + "'"
def body(blocks):
    parts = []
    for k, t in blocks:
        if k == 't': parts.append(t)
        elif k == 'h': parts.append('## ' + t)
        else:
            if EMAIL in t and '](' not in t: t = t.replace(EMAIL, f'[{EMAIL}](mailto:{EMAIL})')
            parts.append(t)
    return '\n\n'.join(parts) + '\n'

if __name__ == '__main__':
    for kind, text in convert(sys.argv[1]):
        print(f'{kind}: {text}')
