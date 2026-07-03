import re

with open(r"E:\Ai\claude xiangmu\portfolio\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Build old and new using indented multi-line strings
old_code = '\t    function openModal(card){\n' \
    '\t      mTitle.textContent=card.title;\n' \
    '\t      mTag.textContent=card.tag;\n' \
    '\t      mTag.style.color=card.color;\n' \
    '\t      mContent.innerHTML=' + "'" + "';\n" \
    '\t\n' \
    '\t      // images section\n' \
    '\t      if(card.images && card.images.length){\n' \
    '\t        var sec=document.createElement(' + "'div'" + ');\n' \
    '\t        sec.className=' + "'mg-section'" + ';\n' \
    '\t        sec.innerHTML=' + "'<div class=\"mg-label\" style=\"color:' + "'+card.color+'" + "'\">" + "\U0001f4f7" + ' 图片</div><div class="mg-grid"></div>' + "';\n" \
    '\t        var grid=sec.querySelector(' + "'.mg-grid'" + ');\n' \
    '\t        card.images.forEach(function(src){\n' \
    '\t          var img=document.createElement(' + "'img'" + ');\n' \
    '\t          img.loading=' + "'lazy'" + ';\n' \
    '\t          img.src=src;\n' \
    '\t          img.addEventListener(' + "'click',function(){ window.open(src,'_blank'); })" + ';\n' \
    '\t          grid.appendChild(img);\n' \
    '\t        });\n' \
    '\t        mContent.appendChild(sec);\n' \
    '\t      }\n' \
    '\t\n' \
    '\t      // videos section\n' \
    '\t      if(card.videos && card.videos.length){\n' \
    '\t        var sec2=document.createElement(' + "'div'" + ');\n' \
    '\t        sec2.className=' + "'mg-section'" + ';\n' \
    '\t        sec2.innerHTML=' + "'<div class=\"mg-label\" style=\"color:' + "'+card.color+'" + "'\">" + "\U0001f3ac" + ' 视频</div><div class="mg-grid"></div>' + "';\n" \
    '\t        var grid2=sec2.querySelector(' + "'.mg-grid'" + ');\n' \
    '\t        card.videos.forEach(function(v){\n' \
    '\t          var vid=document.createElement(' + "'video'" + ');\n' \
    '\t          vid.className=' + "'mg-video'" + ';\n' \
    '\t          vid.controls=true;\n' \
    '\t          vid.preload=' + "'metadata'" + ';\n' \
    '\t          vid.src=v;\n' \
    '\t          grid2.appendChild(vid);\n' \
    '\t        });\n' \
    '\t        mContent.appendChild(sec2);\n' \
    '\t      }\n' \
    '\t\n' \
    '\t      // links section\n' \
    '\t      if(card.links && card.links.length){\n' \
    '\t        var sec3=document.createElement(' + "'div'" + ');\n' \
    '\t        sec3.className=' + "'mg-section'" + ';\n' \
    '\t        sec3.innerHTML=' + "'<div class=\"mg-label\" style=\"color:' + "'+card.color+'" + "'\">" + "\U0001f517" + ' 相关链接</div>' + "';\n" \
    '\t        card.links.forEach(function(lk){\n' \
    '\t          var a=document.createElement(' + "'a'" + ');\n' \
    '\t          a.className=' + "'mg-link'" + ';\n' \
    '\t          a.href=lk.url;\n' \
    '\t          a.target=' + "'_blank'" + ';\n' \
    '\t          a.textContent=lk.label;\n' \
    '\t          sec3.appendChild(a);\n' \
    '\t        });\n' \
    '\t        mContent.appendChild(sec3);\n' \
    '\t      }\n' \
    '\t\n' \
    '\t      // empty fallback\n' \
    '\t      if(!card.images&&!card.videos&&!card.links){\n' \
    '\t        mContent.innerHTML=' + "'<div class=\"mg-empty\">暂无作品内容，后续将补充</div>';\n" \
    '\t      }\n' \
    '\t\n' \
    '\t      overlay.classList.add(' + "'open'" + ');\n' \
    '\t    }'

if old_code in content:
    print("Found old code, proceeding with replacement...")
else:
    print("Old code not found, searching for start marker...")
    idx = content.find('\t      // images section')
    if idx < 0:
        print("ERROR: 'images section' not found. Checking with more tolerance...")
        idx = content.find('images section')
        print(f"Found at {idx}" if idx >= 0 else "Not found at all")
        exit(1)
    print(f"Found at {idx}, trying normalized comparison...")
    # Show first 200 chars of what's around there
    print(repr(content[idx-50:idx+300]))
    exit(1)

# Replace it
print("Replacing...")
content = content.replace(old_code, 'REPLACED_MARKER')

if 'REPLACED_MARKER' in content:
    print("old_code found and replaced with marker")
else:
    print("old_code NOT in content after all")
    exit(1)

print("SUCCESS")
with open(r"E:\Ai\claude xiangmu\portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(content)
