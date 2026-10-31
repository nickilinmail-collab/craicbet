#!/usr/bin/env python3
"""Replace Web Audio API synthetic sound with real MP3 pour sound."""
import re

# New simpler JS: play real mp3 + pour counter
new_js = r'''<script>(function(){
/* Play real pour sound */
var audio=new Audio("/audio/pour.mp3");
audio.volume=0.7;
audio.play().catch(function(){
  document.addEventListener("click",function(){audio.play()},{once:true});
  document.addEventListener("touchstart",function(){audio.play()},{once:true});
});
/* Pour counter */
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
        content = f.read()

    # Replace the old complex Web Audio API script
    old_pattern = r'<script>\(function\(\)\{.*?\}\)\(\);</script>'

    # Find the last occurrence (the preloader script near </body>)
    matches = list(re.finditer(old_pattern, content, flags=re.DOTALL))
    if matches:
        last_match = matches[-1]
        content = content[:last_match.start()] + new_js + content[last_match.end():]
        print(f"Updated {fpath}")
    else:
        print(f"WARNING: No match in {fpath}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done!")
