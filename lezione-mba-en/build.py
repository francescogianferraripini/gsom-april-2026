#!/usr/bin/env python3
"""Build helpers for the English Quantyca deck.

Slide sources live in deck/project/slides/<id>.html (the Slides-artifact format).
Images are referenced either as `ASSET:<path>` (path relative to this folder) or,
once uploaded, as `/_blob/<id>` (mapping kept in blobs.json).

  python build.py html               -> agents-in-action-en.html (standalone viewer)
  python build.py resolve            -> rewrite ASSET:<path> to /_blob/<id> in slide files
  python build.py shot <id> [<id>..] -> render slides to shots/<id>.png and report overflow
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "deck/project/slides"
DECK = HERE / "deck/project/deck.json"
BLOBS = HERE / "blobs.json"
OUT = HERE / "agents-in-action-en.html"


def blobs():
    return json.loads(BLOBS.read_text()) if BLOBS.exists() else {}


def order():
    ids = json.loads(DECK.read_text())["order"]
    extra = sorted(p.stem for p in SLIDES.glob("*.html") if p.stem not in ids)
    return ids + extra


def to_local(html):
    rev = {v: k for k, v in blobs().items()}
    html = re.sub(r'/_blob/[0-9a-f]{32}', lambda m: rev.get(m.group(0), m.group(0)), html)
    return html.replace('src="ASSET:', 'src="')


VIEWER = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agents in Action</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
  html,body{margin:0;height:100%;background:#2a2b2e;overflow:hidden}
  #stage{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:0 0}
  section{position:absolute;inset:0;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden}
  section:not(.on){display:none!important}
  section *{box-sizing:border-box}
  h1,h2,h3,p,ul,ol{margin:0}
  ul,ol{padding-left:1.1em}
  li+li{margin-top:.35em}
  img{display:block}
  aside{display:none}
  table{border-collapse:collapse}
  th,td{padding:.35em .6em;text-align:left;vertical-align:top}
  th{font-weight:600}
  td{border-bottom:1px solid #dee2e6}
  a{color:inherit}
  #hud{position:fixed;right:12px;bottom:8px;font:12px system-ui;color:#999}
  body.all{overflow:auto;background:#555}
  body.all #stage{position:static;transform:none!important;width:1920px;height:auto}
  body.all #stage section{display:flex!important;position:relative;margin:0 0 24px}
  body.all #stage section[style*="display:grid"]{display:grid!important}
  @media print{@page{size:1920px 1080px;margin:0}body{overflow:visible;background:none}#hud{display:none}
    #stage{position:static;transform:none!important}#stage section{display:flex!important;position:relative;break-after:page}
    #stage section[style*="display:grid"]{display:grid!important}}
</style></head><body>
<div id="stage">
__SLIDES__
</div>
<div id="hud"></div>
<script>
const S=[...document.querySelectorAll('#stage>section')];let i=0;
function fit(){const st=document.getElementById('stage');const k=Math.min(innerWidth/1920,innerHeight/1080);
  st.style.transform=`translate(${-960*k}px,${-540*k}px) scale(${k})`;}
function show(n){i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,j)=>s.classList.toggle('on',j===i));
  history.replaceState(null,'','#'+S[i].id);document.getElementById('hud').textContent=(i+1)+' / '+S.length;}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key))show(i+1);
  if(['ArrowLeft','PageUp'].includes(e.key))show(i-1);if(e.key==='Home')show(0);if(e.key==='End')show(S.length-1);});
addEventListener('click',e=>show(e.clientX>innerWidth/3?i+1:i-1));
addEventListener('resize',fit);
if(location.search==='?all'){document.body.classList.add('all');}
else{fit();const h=decodeURIComponent(location.hash.slice(1));const k=S.findIndex(s=>s.id===h);show(k<0?0:k);}
</script></body></html>
"""


def build_html(out=None):
    out = out or OUT
    parts = []
    for sid in order():
        f = SLIDES / f"{sid}.html"
        if f.exists():
            parts.append(to_local(f.read_text().strip()))
    out.write_text(VIEWER.replace("__SLIDES__", "\n".join(parts)))
    print(f"wrote {out} ({len(parts)} slides)")


def resolve():
    m = blobs()
    missing = set()
    for f in SLIDES.glob("*.html"):
        s = f.read_text()
        def sub(mo):
            p = mo.group(1)
            if p in m:
                return f'src="{m[p]}"'
            missing.add(p)
            return mo.group(0)
        n = re.sub(r'src="ASSET:([^"]+)"', sub, s)
        if n != s:
            f.write_text(n)
    if missing:
        print("no blob for:", *sorted(missing), sep="\n  ")


CHECK_JS = """(id)=>{const s=document.getElementById(id);const r=s.getBoundingClientRect();const out=[];
const pad=s.style.paddingBottom;
for(const e of s.querySelectorAll('*')){if(e.closest('aside'))continue;const b=e.getBoundingClientRect();if(!b.width&&!b.height)continue;
 const abs=getComputedStyle(e).position==='absolute';
 const tag=e.tagName.toLowerCase()+(e.textContent?': '+e.textContent.trim().slice(0,40):'');
 if(b.right>r.right+1||b.bottom>r.bottom+1)out.push('OFF-CANVAS '+tag);
 else if(!abs&&!e.closest('[style*=\"position:absolute\"]')&&b.bottom>r.top+924&&s.id!==''&&s.style.paddingBottom==='160px')out.push('PAST y920 '+tag);
 if(['P','H1','H2','H3','LI','TD','TH'].includes(e.tagName)&&(e.scrollWidth>e.clientWidth+2))out.push('TEXT OVERFLOW '+tag);}
return [...new Set(out)].slice(0,12);}"""


def shot(ids):
    from playwright.sync_api import sync_playwright
    import os
    prev = HERE / f".preview-{os.getpid()}.html"
    build_html(prev)
    (HERE / "shots").mkdir(exist_ok=True)
    with sync_playwright() as p:
        import glob, os
        exe = os.environ.get("CHROME") or next(iter(sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/*.app/Contents/MacOS/*")))), None)
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        for sid in ids:
            pg.goto(prev.as_uri() + "?r=" + sid + "#" + sid)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(400)
            pg.screenshot(path=str(HERE / "shots" / f"{sid}.png"))
            issues = pg.evaluate(CHECK_JS, sid)
            print(sid, "OK" if not issues else "\n  " + "\n  ".join(issues))
        b.close()
    prev.unlink()


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "html"
    {"html": build_html, "resolve": resolve}.get(cmd, lambda: shot(sys.argv[2:]))()
