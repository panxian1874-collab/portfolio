p = r'E:\Ai\claude xiangmu\portfolio\index.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

old = '''      if(hasVideos){
        vidPanel=document.createElement('div');
        vidPanel.style.cssText='display:'+(activeTab==='videos'?'flex':'none')+';flex-direction:column;gap:.5rem';
        card.videos.forEach(function(v){
          var vid=document.createElement('video');
          vid.controls=true;
          vid.preload='metadata';
          vid.src=v;
          vid.style.cssText='width:100%;border-radius:8px;border:1px solid var(--line);background:#000;aspect-ratio:16/9;object-fit:contain';
          grid2.appendChild(vid);
        });
        mContent.appendChild(vidPanel);
        vidTab.addEventListener('click',function(){ switchTab('videos'); });
      }'''

new = '''      if(hasVideos){
        vidPanel=document.createElement('div');
        vidPanel.style.cssText='display:'+(activeTab==='videos'?'flex':'none')+';flex-direction:column;gap:.5rem';
        var vidGrid=document.createElement('div');
        vidGrid.className='mg-grid';
        card.videos.forEach(function(v){
          var vid=document.createElement('video');
          vid.controls=true;
          vid.preload='metadata';
          vid.src=v;
          vid.className='mg-video';
          vidGrid.appendChild(vid);
        });
        vidPanel.appendChild(vidGrid);
        mContent.appendChild(vidPanel);
        vidTab.addEventListener('click',function(){ switchTab('videos'); });
      }'''

found = old in c
print(f'found: {found}')
if found:
    c = c.replace(old, new)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print('done')
else:
    idx = c.find('grid2.appendChild')
    print(f'grid2 at index: {idx}')
    print(repr(c[idx-200:idx+100]))
