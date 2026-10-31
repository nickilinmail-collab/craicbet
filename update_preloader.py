#!/usr/bin/env python3
"""Replace preloader in 3 main pages with new version."""
import re

with open('/home/claude/craicbet/preloader.html', 'r') as f:
    new_preloader = f.read().strip()

new_js = r'''<script>(function(){
var audio=new Audio("/audio/pour.mp3");
audio.volume=0.7;
audio.play().catch(function(){
  document.addEventListener("click",function(){audio.play()},{once:true});
  document.addEventListener("touchstart",function(){audio.play()},{once:true});
});
var pct=document.getElementById("pour-pct");
var p=0;
var iv=setInterval(function(){
  p+=2;if(p>100)p=100;
  if(pct)pct.textContent="Pouring your pint... "+p+"%";
  if(p>=100){
    clearInterval(iv);
    if(pct)pct.textContent="Sláinte!";
    setTimeout(function(){
      var el=document.getElementById("preloader");
      if(el){el.style.opacity="0";setTimeout(function(){el.style.display="none"},800)}
      try{audio.pause()}catch(e){}
    },800);
  }
},110);
})();</script>'''

files = [
    '/home/claude/craicbet/index.html',
    '/home/claude/craicbet/ga/index.html',
    '/home/claude/craicbet/pl/index.html',
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pre_start = None
    pre_end = None
    for i, line in enumerate(lines):
        if '<!-- Preloader -->' in line:
            pre_start = i
        if pre_start is not None and '@keyframes x{}' in line:
            pre_end = i
            break

    if pre_start is None or pre_end is None:
        print(f"WARNING: Could not find preloader in {fpath} (start={pre_start}, end={pre_end})")
        continue

    new_lines = lines[:pre_start] + [new_preloader + '\n'] + lines[pre_end+1:]
    content = ''.join(new_lines)

    old_js_pattern = r'<script>\(function\(\)\{.*?\}\)\(\);</script>'
    matches = list(re.finditer(old_js_pattern, content, flags=re.DOTALL))
    if matches:
        last = matches[-1]
        content = content[:last.start()] + new_js + content[last.end():]

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    lc = content.count('\n')
    print(f"OK: {fpath} ({lc} lines)")

print("Done!")
