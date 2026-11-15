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

# ---- export the sentences and the component catalogue as Markdown, so the docs never drift from the demo
def export_docs():
    V=os.path.join(HERE,'views'); un=html.unescape
    def read(n): return open(os.path.join(V,n)).read()
    files=sorted(os.listdir(V))
    lv=[]  # (kind,title,about,[b,a,e])
    for f in files:
        t=read(f); m=re.search(r'^@@levels (.*)$',t,re.M)
        if not m: continue
        title=re.search(r'data-title="([^"]*)"',t).group(1)
        about=un(re.search(r'<section class="anat">.*?<p class="measure">(.*?)</p>',t,re.S).group(1))
        lv.append(('voice' if 'voice-' in f else 'recipe',title,about,[x.strip() for x in m.group(1).split('||')]))
    parts=[]
    for sec in re.findall(r'<section class="spec".*?</section>',read('30-parts.html'),re.S):
        q,effort,made,grow,use=[x.strip() for x in re.search(r'^@@ask (.*)$',sec,re.M).group(1).split('||')]
        parts.append((re.search(r'<h2>(.*?)</h2>',sec).group(1),un(re.search(r'<p class="measure">(.*?)</p>',sec,re.S).group(1)),un(q),effort,made,grow,use))
    photo=[]; pt=read('20-photo.html')
    for sec in re.findall(r'<section class="spec".*?</section>',pt,re.S):
        name=re.search(r'<h2>(.*?)</h2>',sec).group(1); facts=dict((a,un(b)) for a,b in re.findall(r'<dt>(.*?)</dt><dd>(.*?)</dd>',sec))
        q=re.search(r'<blockquote[^>]*>(.*?)</blockquote>',sec,re.S).group(1).strip()
        photo.append((name,un(re.search(r'<p class="measure">(.*?)</p>',sec,re.S).group(1)),un(q),facts['Effort'],facts['Made here with'],facts['Grow into'],facts['Seen in']))
    looks=re.findall(r"\{id:'(\w+)',name:'([^']+)',line:'([^']+)',voice:'([^']+)',by:'([^']+)',ask:'([^']+)'\}",pt)
    o=['# Sentences','','Every sentence in the studio, in one place. Copy one, attach your notes (and a photo if the page uses one), and paste both into a chat assistant.','',
       '**Status: untested.** These sentences describe what the demo pages do. They have not yet been run in fresh chats and scored. Record results in [`sentence-test.md`](sentence-test.md).','',
       'This file is generated from the demo by `level-demo/source/build.py`. Edit the views, not this file.','']
    for kind,head in (('recipe','Recipes'),('voice','Voices')):
        o+=[f'## {head}','']
        for k,title,about,(b,a,e) in lv:
            if k!=kind: continue
            o+=[f'### {title}','',about,'',f'- **Beginner:** {b}',f'- **Advanced:** {a}',f'- **Expert:** {e}','']
    for head,rows,last in (('Page components',parts,'Use it for'),('Photo components',photo,'Seen in')):
        o+=[f'## {head}','']
        for name,blurb,q,effort,made,grow,use in rows:
            if name=='Looks and voices':
                o+=[f'### {name}','',blurb,'']+[f'- **{n}:** {a}' for i,n,line,voice,by,a in looks]+['']; continue
            o+=[f'### {name}','',blurb,'',f'> {q}','',f'Effort: {effort} {last}: {use.rstrip(".")}.','']
    open(os.path.join(HERE,'..','..','level-simple','sentences.md'),'w').write('\n'.join(o).rstrip()+'\n')
    c=['# Component catalogue','','The parts a page can be built from. Each row is a working example in the studio demo. Pick parts that carry content; never add one for decoration.','',
       'Generated from the demo by `drafts/artifact-studio/level-demo/source/build.py`.','']
    for head,rows in (('Page components (no photo needed)',parts),('Photo components',photo)):
        c+=[f'## {head}','','| Component | What it is for | How it is made | Grow into |','| --- | --- | --- | --- |']
        c+=[f'| {n} | {b} | {made} | {grow} |' for n,b,q,effort,made,grow,use in rows]+['']
    sk=os.path.join(HERE,'..','..','..','..','skills','artifact-studio','references','components.md')
    open(sk,'w').write('\n'.join(c).rstrip()+'\n'); print('docs:',len(lv),'level sets,',len(parts),'page parts,',len(photo),'photo parts')
export_docs()

# ---- the one-page explainer saved in docs/ (built with the studio's own recipe and voice)
SCORES=[('Teaching and promo',85,90),('Stunning, with tone',80,86),('Easy for a non-coder',70,76),('Fits the level ladder',60,88),('Reuse before build',45,58),('Evidence',45,62),('Business usefulness',40,80)]
def build_explained():
    t=open(os.path.join(HERE,'explained.src.html')).read()
    f2=[x for x in ff if x[3] in ('np7','np4','cp4','cp4i')]
    fonts2='\n'.join(f'@font-face{{font-family:"{n}";font-weight:{w};font-style:{s};font-display:swap;src:url(data:font/woff2;base64,{A["fonts"][k]}) format("woff2")}}' for n,w,s,k in f2)
    bars=''.join(f'<div class="hb-row"><span class="hb-l">{n}</span><span class="hb-t"><span><i class="q" style="--v:{b*.8:.0f}%"></i><b>{b}</b></span><span><i style="--v:{a*.8:.0f}%"></i><b>{a}</b></span></span></div>' for n,b,a in SCORES)
    t=t.replace('/*FONTS*/',fonts2).replace('/*PHOTO*/',f'--photo:url("data:image/jpeg;base64,{A["sunset"]}");').replace('__BARS__',bars)
    out=os.path.join(HERE,'..','..','..','..','docs','artifact-studio-explained.html'); open(out,'w').write(t)
    print('explained:',round(len(t.encode())/1024),'KB; overall before',round(sum(b for _,b,_ in SCORES)/len(SCORES)),'after',round(sum(a for _,_,a in SCORES)/len(SCORES)))
build_explained()
