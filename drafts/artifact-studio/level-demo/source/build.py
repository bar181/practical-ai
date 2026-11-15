"""Assemble artifact-studio.html from shell.html, base.css, the views folder and assets.json.

Usage: python3 prepare_assets.py ... then python3 build.py
Each file in views/ holds one tab or page: an optional <style>, the markup (a div.view with id v-NAME),
and an optional <script> that registers onView("NAME", root => { ... }) to run the first time it is shown.
Two macros keep the views short:
  @@ask sentence || effort || made here with || grow into || use it for
  @@levels beginner sentence || advanced sentence || expert sentence
"""
import json, os, re, glob, html
HERE=os.path.dirname(os.path.abspath(__file__))
A=json.load(open(os.path.join(HERE,'assets.json')))
ff=[('National Park',700,'normal','np7'),('National Park',400,'normal','np4'),('Crimson Pro',400,'normal','cp4'),('Crimson Pro',400,'italic','cp4i'),('Crimson Pro',700,'normal','cp7'),
    ('Instrument Sans',400,'normal','is4'),('Instrument Sans',700,'normal','is7'),('JetBrains Mono',400,'normal','jb4'),('Gloock',400,'normal','gl4'),('Big Shoulders',700,'normal','bs7'),
    ('Work Sans',400,'normal','ws4'),('Work Sans',700,'normal','ws7'),('IBM Plex Serif',400,'normal','px4'),('IBM Plex Serif',400,'italic','px4i'),('IBM Plex Serif',700,'normal','px7')]
fonts='\n'.join(f'@font-face{{font-family:"{n}";font-weight:{w};font-style:{s};font-display:swap;src:url(data:font/woff2;base64,{A["fonts"][k]}) format("woff2")}}' for n,w,s,k in ff)
P=A['paths']
order=[('tree',0,.26,''),('shore',.06,.24,'thin'),('isl',.2,.16,''),('trunkL',.3,.2,''),('trunkR',.34,.2,''),('bark',.42,.16,'thin'),('branches',.44,.2,''),('bush',.5,.08,''),('ripples',.5,.16,'thin'),('reeds',.56,.22,'thin'),('cattails',.66,.12,''),('ground',.7,.08,'')]
paths=''.join(f'<path pathLength="1" class="{c}" style="--s:{s};--d:{d}" d="{P[k]}"/>' for k,s,d,c in order)

def ask_macro(m):
    q,effort,made,grow,use=[x.strip() for x in m.group(1).split('||')]
    return (f'<div class="recipe wrap"><div class="ask"><h3>Ask for it like this</h3><blockquote>{q}</blockquote><button class="copy" type="button">Copy</button></div>'
            f'<dl class="facts"><div><dt>Effort</dt><dd>{effort}</dd></div><div><dt>Made here with</dt><dd>{made}</dd></div><div><dt>Grow into</dt><dd>{grow}</dd></div><div><dt>Use it for</dt><dd>{use}</dd></div></dl></div>')
def levels_macro(m):
    b,a,e=[x.strip() for x in m.group(1).split('||')]
    rows=[('Beginner','one sentence',b),('Advanced','add your look, voice and parts',a),('Expert','hand the whole job to the skill',e)]
    return '<div class="levels">'+''.join(f'<div class="ask"><h3><b>{n}:</b> {d}</h3><blockquote>{q}</blockquote><button class="copy" type="button">Copy</button></div>' for n,d,q in rows)+'</div>'

css=[];body=[];js=[];names=[]
for f in sorted(glob.glob(os.path.join(HERE,'views','*.html'))):
    t=open(f).read()
    for m in re.finditer(r'<style>(.*?)</style>',t,re.S): css.append(m.group(1).strip())
    for m in re.finditer(r'<script>(.*?)</script>',t,re.S): js.append(m.group(1).strip())
    t=re.sub(r'<style>.*?</style>|<script>.*?</script>','',t,flags=re.S).strip()
    t=re.sub(r'^@@ask (.*)$',ask_macro,t,flags=re.M); t=re.sub(r'^@@levels (.*)$',levels_macro,t,flags=re.M)
    m=re.search(r'id="v-([\w-]+)"',t)
    if not m: continue
    names.append((m.group(1),re.search(r'data-title="([^"]*)"',t).group(1) if 'data-title' in t.split('>')[0] else m.group(1),t)); 
# pagers for voice and recipe pages
out=[]
for kind,label in (('voice','voices'),('recipe','recipes')):
    grp=[n for n in names if n[0].startswith(kind+'-')]
    for i,(nm,title,t) in enumerate(grp):
        prev=grp[i-1]; nxt=grp[(i+1)%len(grp)]
        crumb=f'<div class="crumb"><a href="#{label}" data-go="{label}">All {label}</a><span>{html.escape(title)}</span></div>'
        pager=f'<nav class="pager" aria-label="More {label}"><div><a href="#{prev[0]}" data-go="{prev[0]}">← {html.escape(prev[1])}</a><a href="#{nxt[0]}" data-go="{nxt[0]}">{html.escape(nxt[1])} →</a></div></nav>'
        t2=re.sub(r'(<div class="view"[^>]*>)',lambda m:m.group(1)+crumb,t,count=1); t2=t2[:t2.rindex('</div>')]+pager+'</div>'
        names[names.index((nm,title,t))]=(nm,title,t2)
body=[t for _,_,t in names]
t=open(os.path.join(HERE,'shell.html')).read()
photos=f'--photo:url("data:image/jpeg;base64,{A["photo"]}");--photo2:url("data:image/jpeg;base64,{A["sunset"]}");'
data=json.dumps({'rows':A['rows'],'pal':A['pal']},separators=(',',':'))
t=t.replace('/*FONTS*/',fonts).replace('/*PHOTOS*/',photos).replace('/*BASE_CSS*/',open(os.path.join(HERE,'base.css')).read())
t=t.replace('/*VIEW_CSS*/','\n'.join(css)).replace('<!--VIEWS-->','\n'.join(body)).replace('<!--VIEW_JS-->','<script>\n'+'\n'.join(js)+'\n</script>')
t=t.replace('__PATHS__',paths).replace('__DATA__',data).replace('__TOPHEX__',A['pal'][0]['hex']).replace('__TOPSHARE__',str(round(A['pal'][0]['share'])))
kb=round(len(t.encode())/1024); t=t.replace('__KB__',f'{kb:,}')
left=re.findall(r'__[A-Z]+__|^@@\w+',re.sub(r'data:[^")]+','',t),flags=re.M); assert not left, left
open(os.path.join(HERE,'..','artifact-studio.html'),'w').write(t); print('built',kb,'KB;',len(names),'views:',' '.join(n for n,_,_ in names))
