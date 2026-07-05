p = r'E:\Ai\claude xiangmu\portfolio\index.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace(
    '.mg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:.8rem}',
    '.mg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:.5rem}'
)
c = c.replace(
    '.mg-grid img{width:100%;border-radius:10px;',
    '.mg-grid img{width:100%;border-radius:8px;'
)
c = c.replace(
    '.mg-video{width:100%;border-radius:10px;border:1px solid var(--line);background:#000;aspect-ratio:16/9;object-fit:contain;cursor:pointer}',
    '.mg-video{width:100%;border-radius:8px;border:1px solid var(--line);background:#000;aspect-ratio:16/9;object-fit:contain;cursor:pointer}'
)
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)
print('done')
