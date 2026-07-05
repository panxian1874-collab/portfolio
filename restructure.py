import re

p = r'E:\Ai\claude xiangmu\portfolio\index.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1) Remove floating cards HTML div
c = c.replace('<!-- ===== Floating Portfolio Cards ===== -->\n<div id="floatingCards"></div>\n', '')

# 2) Add showcase section before CONTACT
showcase_html = '''<!-- ============ SHOWCASE ============ -->
<section id="showcase">
  <span class="eyebrow">PORTFOLIO · 作品展示</span>
  <h2 class="sec-title hglitch">作品集<span class="en">My Works</span></h2>
  <div class="sw-tabs" id="swTabs">
    <button class="sw-tab active" data-tab="design">日常设计</button>
    <button class="sw-tab" data-tab="video">视频作品</button>
    <button class="sw-tab" data-tab="red">小红书账号</button>
    <button class="sw-tab" data-tab="event">活动内容</button>
  </div>
  <div class="sw-panels">
    <div class="sw-panel active" id="swDesign"><div class="mg-grid">'''

# Collect all images
all_images = [
    'images/event/1.benner.png',
    'images/event/主视觉.png',
    'images/event/线下拍摄.png',
    'images/ip/ip设计.png',
    'images/social/ScreenShot_2026-07-03_165951_174.png',
    'images/social/ScreenShot_2026-07-03_170725_793.png',
    'images/social/ScreenShot_2026-07-03_172823_629.png',
    'images/social/宣传图.png',
    'images/airline/新客專享券包_9比16海報.png'
]
for src in all_images:
    showcase_html += f'\n      <img loading="lazy" src="{src}" onclick="window.open(\'{src}\',\'_blank\')">'

showcase_html += '''
    </div></div>
    <div class="sw-panel" id="swVideo"><div class="mg-grid">'''

# Collect all videos
all_videos = [
    'videos/event/1(1).mp4', 'videos/event/航旅2.mp4', 'videos/event/航旅封面高码率.mp4',
    'videos/ip/小美ai.mp4', 'videos/ip/ip形象节日视频.mp4', 'videos/ip/财神日.mp4',
    'videos/ip/七一香港回归.mp4', 'videos/ip/七夕.mp4', 'videos/ip/中秋.mp4',
    'videos/ip/元旦.mp4', 'videos/ip/圣诞节.mp4', 'videos/social/5.mp4',
    'videos/airline/达美视频-导出.mp4'
]
for src in all_videos:
    showcase_html += f'\n      <video class="mg-video" controls preload="metadata" src="{src}"></video>'

showcase_html += '''
    </div></div>
    <div class="sw-panel" id="swRed"><div class="mg-empty">小红书双账号运营作品整理中，即将上线</div></div>
    <div class="sw-panel" id="swEvent"><div class="mg-empty">大型线下活动影像记录整理中，即将上线</div></div>
  </div>
</section>

'''

# Insert before CONTACT
c = c.replace('<!-- ============ CONTACT ============ -->', showcase_html + '<!-- ============ CONTACT ============ -->')

# 3) Remove the entire initFloatingCards function (including the modal open/close/modalData parts)
# Find the marker and remove everything from "/* ---- Floating Portfolio Cards" until after cardData.forEach loop + electric border
start_marker = '  /* ---- Floating Portfolio Cards with Electric Border + Modal ---- */'
end_marker = '\n  /* ---- nav highlight ---- */'
idx_start = c.find(start_marker)
idx_end = c.find(end_marker)
if idx_start != -1 and idx_end != -1:
    # Find the actual function end - go past cardData and forEach
    # Look for the next known function/comment marker after the floating cards code
    after_floating = c.find('\n  /* ---- click spark ---- */')
    if after_floating != -1:
        c = c[:idx_start] + c[after_floating:]
        print(f'Removed floating cards JS from {idx_start} to {after_floating}')
    else:
        print('Could not find click spark marker')
else:
    print(f'start_marker found: {idx_start}, end_marker found: {idx_end}')

# 4) Add CSS for showcase tabs
showcase_css = '''
/* ---- Showcase Section ---- */
#showcase .sw-tabs{display:flex;gap:.5rem;margin-bottom:1.5rem;flex-wrap:wrap}
#showcase .sw-tab{padding:.6rem 1.4rem;border:1.5px solid var(--line);border-radius:999px;
  background:transparent;color:var(--ink-soft);font-family:"Space Grotesk",sans-serif;
  font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700;
  cursor:pointer;transition:.25s}
#showcase .sw-tab:hover{border-color:var(--cyan);color:var(--cyan)}
#showcase .sw-tab.active{background:var(--cyan);color:#08070d;border-color:var(--cyan);box-shadow:0 0 20px -6px var(--cyan)}
#showcase .sw-panel{display:none}
#showcase .sw-panel.active{display:block}
'''

# Insert after the mg-empty CSS
c = c.replace('.mg-empty{text-align:center;padding:1.5rem;color:var(--ink-soft);font-family:"VT323",monospace;font-size:.95rem;\n  border:1.5px dashed var(--line);border-radius:12px}',
    '.mg-empty{text-align:center;padding:1.5rem;color:var(--ink-soft);font-family:"VT323",monospace;font-size:.95rem;\n  border:1.5px dashed var(--line);border-radius:12px}' + showcase_css)

# 5) Add tab switching JS at the end of the script
tab_js = '''
  /* ---- Showcase Tabs ---- */
  (function(){
    var tabs=document.querySelectorAll('.sw-tab');
    var panels={design:document.getElementById('swDesign'),video:document.getElementById('swVideo'),red:document.getElementById('swRed'),event:document.getElementById('swEvent')};
    tabs.forEach(function(tab){
      tab.addEventListener('click',function(){
        tabs.forEach(function(t){t.classList.remove('active');});
        tab.classList.add('active');
        Object.keys(panels).forEach(function(k){panels[k].classList.remove('active');});
        var target=panels[tab.getAttribute('data-tab')];
        if(target) target.classList.add('active');
      });
    });
  })();
'''

# Insert at the end of the script block (before </script>)
c = c.replace('</script>', tab_js + '</script>')

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)
print('done')
