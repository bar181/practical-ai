"""Assemble the four studio pages (all examples, and one per level) from shell.html, base.css, the views folder and assets.json.

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

import markdown
ROOT=os.path.normpath(os.path.join(HERE,'..','..'))            # drafts/artifact-studio
SKILL=os.path.normpath(os.path.join(ROOT,'..','..','skills','artifact-studio'))
def md_html(path,drop_h1=False):
    src=open(path).read()
    if src.startswith('---'):
        _,fm,src=src.split('---',2); src='```\n'+fm.strip()+'\n```\n'+src
    h=markdown.markdown(src,extensions=['tables','fenced_code','sane_lists'])
    if drop_h1: h=re.sub(r'<h1>.*?</h1>','',h,count=1,flags=re.S)
    h=re.sub(r'<a href="(?!https?:)[^"]*">(.*?)</a>',r'\1',h,flags=re.S)       # repo-relative links mean nothing inside an artifact
    h=h.replace('<table>','<div class="tblw" tabindex="0" role="region" aria-label="Table"><table>').replace('</table>','</table></div>')
    h=re.sub(r'<th></th>','<td></td>',h)
    h=re.sub(r'<li>\[ \] ?(.*?)</li>',r'<li class="task"><label><input type="checkbox"><span>\1</span></label></li>',h,flags=re.S)
    h=re.sub(r'<pre>(.*?)</pre>',r'<div class="codeb"><pre>\1</pre><button class="copy" type="button">Copy</button></div>',h,flags=re.S)
    return h
def md_macro(m): return '<article class="md sub"><div class="wrap">'+md_html(os.path.normpath(os.path.join(ROOT,m.group(1).strip())),drop_h1=True)+'</div></article>'
def md_view(name,title,path,raw=None):
    if raw: inner=f'<h1>{html.escape(title)}</h1><p>{raw}</p><div class="codeb"><pre>{html.escape(open(path).read().strip())}</pre><button class="copy" type="button">Copy</button></div>'
    else: inner=md_html(path)
    return f'<div class="view" id="v-{name}" data-title="{html.escape(title)}"><article class="md"><div class="wrap">{inner}</div></article></div>'

# every view file: css always, script and markup kept by name
css=[];VIEW={};VJS={};LIB=[]
for f in sorted(glob.glob(os.path.join(HERE,'views','*.html'))):
    t=open(f).read()
    for m in re.finditer(r'<style>(.*?)</style>',t,re.S): css.append(m.group(1).strip())
    sc=[m.group(1).strip() for m in re.finditer(r'<script>(.*?)</script>',t,re.S)]
    t=re.sub(r'<style>.*?</style>|<script>.*?</script>','',t,flags=re.S).strip()
    t=re.sub(r'^@@ask (.*)$',ask_macro,t,flags=re.M); t=re.sub(r'^@@levels (.*)$',levels_macro,t,flags=re.M); t=re.sub(r'^\s*@@md (.*)$',md_macro,t,flags=re.M)
    m=re.search(r'id="v-([\w-]+)"',t)
    if not m: LIB+=sc; continue
    VIEW[m.group(1)]=t; VJS[m.group(1)]=sc
MD={ # name: (title, path, note shown above a copy-ready block or None to render the Markdown)
 'l1-sentences':('All sentences',ROOT+'/level-simple/sentences.md',None),
 'l1-test':('Test a sentence',ROOT+'/level-simple/sentence-test.md',None),
 'l2-recipes':('Recipe cards',SKILL+'/references/recipes.md',None),
 'l2-voices':('Voice cards',SKILL+'/references/voices.md',None),
 'l2-parts':('Parts list',SKILL+'/references/components.md',None),
 'l2-spec':('Design spec',ROOT+'/level-working/design-spec-template.md','Fill this in once and keep it. Attach it to every request so each page comes out in your colours and type. Copy it, then replace the parts in brackets.'),
 'l2-brief':('Content brief',ROOT+'/level-working/content-brief-template.md','Fill this in for each page. Five lines that tell the assistant who the page is for and what it must do. Copy it, then replace the parts in brackets.'),
 'l3-skill':('The skill',SKILL+'/SKILL.md',None),
 'l3-single':('Single-file edition',SKILL+'/SKILL-single-file.md','The whole skill condensed into one file, for assistants that cannot load a skill folder. Copy it and paste it into the instructions of a Project.'),
 'l3-skel':('Page skeleton',SKILL+'/assets/page-skeleton.html','The starting file the skill builds from. One self-contained page with the tokens, the type scale and the motion rules already in place.'),
 'l3-rules':('Build rules',SKILL+'/references/build-rules.md',None),
 'l3-check':('Pre-ship checklist',SKILL+'/references/pre-ship-checklist.md',None),
 'l3-agent':('Agent guide',ROOT+'/AGENT-GUIDE.md',None),
 'l3-best':('Best practices',ROOT+'/BEST-PRACTICES.md',None)}
for n,(title,path,raw) in MD.items(): VIEW[n]=md_view(n,title,path,raw); VJS[n]=[]
LABEL={'voice-keynote':'Keynote','voice-story':'Storyteller','voice-teacher':'Teacher','voice-pitch':'Pitch','voice-practical':'Practical','voice-analyst':'Analyst','voice-brief':'Brief',
       'recipe-report':'Report','recipe-proposal':'Proposal','recipe-explainer':'Explainer','recipe-landing':'Landing page'}
VOICES=['voice-keynote','voice-story','voice-teacher','voice-pitch','voice-practical','voice-analyst','voice-brief']
RECIPES=['recipe-report','recipe-proposal','recipe-explainer','recipe-landing']
G_VOICES=('Voices',VOICES,'One message, told seven ways. Tap a voice:'); G_RECIPES=('Recipes',RECIPES,'Four whole pages. Tap a recipe:')
EDITIONS={ # each: output file, title, one-line lead, groups of (tab label, [views], caption for the second row)
 'all':('level-demo/artifact-studio.html','All examples','Seven voices, 24 parts and four whole pages. Tap a tab. Every example shows the sentence that asks for it.',
   [G_VOICES,('Photo parts',['photo'],''),('Page parts',['parts'],''),G_RECIPES]),
 'beginner':('level-simple/artifact-studio-beginner.html','Level 1: Beginner','One sentence gets you a page. Find an example you like and copy its sentence.',
   [('Start here',['l1-start'],''),G_RECIPES,('Photo parts',['photo'],''),('Page parts',['parts'],''),('Sentences',['l1-sentences','l1-test'],'Every sentence on one page, and how to test one:')]),
 'advanced':('level-working/artifact-studio-advanced.html','Level 2: Advanced','You choose the voice, the look and the parts, so the page sounds and looks like yours.',
   [('Start here',['l2-start'],''),G_VOICES,('Looks',['l2-looks'],''),('Mix',['l2-mix'],''),('Cards',['l2-recipes','l2-voices','l2-parts'],'The reference cards to keep in your Project:'),('Templates',['l2-spec','l2-brief'],'Two short forms to copy and fill in:')]),
 'expert':('level-automated/artifact-studio-expert.html','Level 3: Expert','Hand over any content and media. The skill chooses, builds, checks and reports what it assumed.',
   [('Start here',['l3-start'],''),('The skill',['l3-skill','l3-single','l3-skel'],'Three forms of the same instructions:'),('Build rules',['l3-rules'],''),('Checklist',['l3-check'],''),('Agent guide',['l3-agent'],''),('Best practices',['l3-best'],'')]),
}
# a short "about" strip at the top of every voice and recipe tab, taken from the voice cards and from the page's own closing note
_v=open(SKILL+'/references/voices.md').read()
_use={n.strip():u.strip() for u,n in re.findall(r'^\| ([^|]+) \| ([^|]+) \|$',_v[_v.index('## Choosing'):_v.index('## Keynote')],re.M) if n.strip() not in ('Use','---')}
_by=dict(re.findall(r'^## ([^\n]+)\n\n\| Field \| \|\n\| --- \| --- \|\n\| Inspired by \| ([^|]+) \|',_v,re.M))
VNAME={'voice-keynote':'Keynote','voice-story':'Storyteller','voice-teacher':'Teacher','voice-pitch':'Pitch','voice-practical':'Practical instructor','voice-analyst':'Analyst','voice-brief':'Executive brief'}
def about(n,t):
    if n in VNAME:
        k=VNAME[n]; u=_use[k]; by=_by[k].strip(); by=by[0].lower()+by[1:] if by.startswith(('The ','A ')) else by; txt=f'<b>The {k.lower()} voice.</b> Inspired by {html.escape(by)}. Use it when the reader should {u[0].lower()+u[1:]}.'
        note='A full example follows.'
    elif n.startswith('recipe-'):
        m=re.search(r'<section class="anat">.*?<p class="measure">(.*?)</p>',t,re.S); first=re.split(r'(?<=\.) ',m.group(1).strip())[0]
        txt=f'<b>The {re.search(chr(100)+'ata-title="([^"]*)"',t).group(1).lower()} recipe.</b> {first}'; note='A full example follows, with invented content.'
    else: return t
    strip=f'<aside class="about" aria-label="About this example"><div class="wrap"><p>{txt}</p><p class="about-n">{note} <a href="#anat-{n}" data-jump="anat-{n}">How it is built, and the sentence that asks for it</a></p></div></aside>'
    t=t.replace('<section class="anat">',f'<section class="anat" id="anat-{n}">',1)
    return re.sub(r'(<div class="view"[^>]*>)',lambda m:m.group(1)+strip,t,count=1)
SHELL=open(os.path.join(HERE,'shell.html')).read()
BASE=open(os.path.join(HERE,'base.css')).read()
data=json.dumps({'rows':A['rows'],'pal':A['pal']},separators=(',',':'))
def title_of(n): return LABEL.get(n) or re.search(r'data-title="([^"]*)"',VIEW[n]).group(1)
def build(key):
    out,title,lead,groups=EDITIONS[key]
    order=[n for _,vs,_ in groups for n in vs]
    radios=[];g_row=[];s_rows=[];tcss=[]
    for i,(gl,vs,cap) in enumerate(groups):
        for n in vs:
            radios.append(f'<input class="tabr" type="radio" name="tab" id="t-{n}" aria-label="{html.escape(gl if len(vs)==1 else gl+": "+VNAME.get(n,title_of(n)))}"{" checked" if n==order[0] else ""}>')
            tcss.append(f'#t-{n}:checked~#v-{n}{{display:block}}\n#t-{n}:focus-visible~.tabs label[for="t-{n}"]{{outline:3px solid var(--reed);outline-offset:2px}}')
            if len(vs)>1: tcss.append(f'#t-{n}:checked~.tabs .tabs-s label[for="t-{n}"]{{background:var(--reed);color:var(--pine)}}')
        sel=':is('+','.join('#t-'+n for n in vs)+'):checked~.tabs '
        tcss.append(sel+f'.g{i}{{background:var(--fog);color:var(--pine);border-color:var(--fog)}}')
        g_row.append(f'<label class="g{i}" for="t-{vs[0]}">{html.escape(gl)}</label>')
        if len(vs)>1:
            tcss.append(sel+f'.s{i}{{display:flex}}')
            s_rows.append(f'<div class="tabs-s s{i}"><span>{html.escape(cap)}</span>'+''.join(f'<label for="t-{n}">{html.escape(title_of(n))}</label>' for n in vs)+'</div>')
    nav='<nav class="tabs" aria-label="Sections"><div class="tabs-g">'+''.join(g_row)+'</div>'+''.join(s_rows)+'</nav>'
    mast=f'<header class="mast"><div class="wrap"><p class="mast-t"><span>Artifact studio</span> {html.escape(title)}</p><p class="mast-l">{html.escape(lead)}</p></div></header>'
    body=[]
    for k,n in enumerate(order):
        t=about(n,VIEW[n]); prev=order[k-1] if k else None; nxt=order[k+1] if k+1<len(order) else None
        pager='<nav class="pager" aria-label="Previous and next tab"><div>'+(f'<label for="t-{prev}">← {html.escape(title_of(prev))}</label>' if prev else '<span></span>')+(f'<label for="t-{nxt}">{html.escape(title_of(nxt))} →</label>' if nxt else '<span></span>')+'</div></nav>'
        body.append(t[:t.rindex('</div>')]+pager+'</div>')
    js=LIB+[x for n in order for x in VJS[n]]
    js='\n'.join('try{(()=>{\n'+x+'\n})()}catch(err){console.error(err)}' for x in js)
    photos='' if key=='expert' else f'--photo:url("data:image/jpeg;base64,{A["photo"]}");--photo2:url("data:image/jpeg;base64,{A["sunset"]}");'
    t=SHELL.replace('<title>Artifact studio</title>',f'<title>Artifact studio: {html.escape(title)}</title>')
    t=t.replace('/*FONTS*/',fonts).replace('/*PHOTOS*/',photos).replace('/*BASE_CSS*/',BASE).replace('/*TAB_CSS*/','\n'.join(tcss)).replace('/*VIEW_CSS*/','\n'.join(css))
    t=t.replace('<!--MAST-->',mast).replace('<!--RADIOS-->','\n'.join(radios)).replace('<!--NAV-->',nav).replace('<!--VIEWS-->','\n'.join(body)).replace('/*VIEW_JS*/',js)
    t=t.replace('__PATHS__',paths).replace('__DATA__',data).replace('__TOPHEX__',A['pal'][0]['hex']).replace('__TOPSHARE__',str(round(A['pal'][0]['share'])))
    kb=round(len(t.encode())/1024); t=t.replace('__KB__',f'{kb:,}')
    left=re.findall(r'__[A-Z]+__|^\s*@@\w+',re.sub(r'data:[^")]+','',re.sub(r'<pre>.*?</pre>','',t,flags=re.S)),flags=re.M); assert not left, left
    open(os.path.join(ROOT,out),'w').write(t); print(f'{key}: {kb} KB, {len(order)} tabs -> {out}')
for key in EDITIONS: build(key)

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
SCORES=[('Teaching and promo',85,90),('Stunning, with tone',80,86),('Easy for a non-coder',70,74),('Fits the level ladder',60,90),('Reuse before build',45,58),('Evidence',45,64),('Business usefulness',40,80)]
def build_explained():
    t=open(os.path.join(HERE,'explained.src.html')).read()
    f2=[x for x in ff if x[3] in ('np7','np4','cp4','cp4i')]
    fonts2='\n'.join(f'@font-face{{font-family:"{n}";font-weight:{w};font-style:{s};font-display:swap;src:url(data:font/woff2;base64,{A["fonts"][k]}) format("woff2")}}' for n,w,s,k in f2)
    bars=''.join(f'<div class="hb-row"><span class="hb-l">{n}</span><span class="hb-t"><span><i class="q" style="--v:{b*.8:.0f}%"></i><b>{b}</b></span><span><i style="--v:{a*.8:.0f}%"></i><b>{a}</b></span></span></div>' for n,b,a in SCORES)
    t=t.replace('/*FONTS*/',fonts2).replace('/*PHOTO*/',f'--photo:url("data:image/jpeg;base64,{A["sunset"]}");').replace('__BARS__',bars)
    out=os.path.join(HERE,'..','..','..','..','docs','practical-ai-explained.html'); open(out,'w').write(t)
    print('explained:',round(len(t.encode())/1024),'KB; overall before',round(sum(b for _,b,_ in SCORES)/len(SCORES)),'after',round(sum(a for _,_,a in SCORES)/len(SCORES)))
build_explained()
