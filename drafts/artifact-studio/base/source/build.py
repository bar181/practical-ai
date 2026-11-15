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
    rows=[('Short ask','one sentence',b),('Full ask','you name the voice, look and parts',a),('With the skill','it does the whole job',e)]
    return '<div class="levels">'+''.join(f'<div class="ask"><h3><b>{n}:</b> {d}</h3><blockquote>{q}</blockquote><button class="copy" type="button">Copy</button></div>' for n,d,q in rows)+'</div>'

import markdown, base64
import catalog as C
ROOT=os.path.normpath(os.path.join(HERE,'..','..'))            # drafts/artifact-studio
SKILL=os.path.normpath(os.path.join(ROOT,'..','..','skills','artifact-studio'))
def md_html(path,drop_h1=False):
    src=open(path).read()
    if src.startswith('---'):
        _,fm,src=src.split('---',2); src='```\n'+fm.strip()+'\n```\n'+src
    src=re.sub(r'\n## The level \d page\n.*?(?=\n## )','',src,flags=re.S)                 # a page need not describe itself
    def flow(m):                                                                          # a Mermaid flowchart becomes a plain stack of steps
        steps=list(dict.fromkeys(re.findall(r'\[([^\]]+)\]',m.group(1)))); back=re.search(r'--\s*([^-\n]+?)\s*-->',m.group(1))
        return '<ol class="flow">'+''.join(f'<li>{html.escape(re.sub(r"^\d+\.\s*","",x))}</li>' for x in steps)+'</ol>'+(f'<p class="flow-n">If the check {html.escape(back.group(1))}, go back to the outline and fix it.</p>' if back else '')
    src=re.sub(r'```mermaid\n(.*?)```',flow,src,flags=re.S)
    h=markdown.markdown(src,extensions=['tables','fenced_code','sane_lists'])
    if drop_h1: h=re.sub(r'<h1>.*?</h1>','',h,count=1,flags=re.S)
    h=re.sub(r'<a href="(?!https?:)[^"]*">(.*?)</a>',r'\1',h,flags=re.S)       # repo-relative links mean nothing inside an artifact
    h=h.replace('<table>','<div class="tblw" tabindex="0" role="region" aria-label="Table"><table>').replace('</table>','</table></div>')
    h=re.sub(r'<th></th>','<td></td>',h)
    h=re.sub(r'<li>\[ \] ?(.*?)</li>',r'<li class="task"><label><input type="checkbox"><span>\1</span></label></li>',h,flags=re.S)
    h=re.sub(r'<pre>(.*?)</pre>',r'<div class="codeb"><pre>\1</pre><button class="copy" type="button">Copy</button></div>',h,flags=re.S)
    return h
SVGDIR=os.path.normpath(os.path.join(HERE,'..','templates','components','svg'))
def svg_items():
    out=[]
    for f in sorted(glob.glob(os.path.join(SVGDIR,'*.svg'))):
        t=open(f).read(); out.append((os.path.basename(f),re.search(r'<title[^>]*>(.*?)</title>',t).group(1),re.search(r'<desc>(.*?)</desc>',t).group(1),t))
    return out
def svgset_macro(m):
    rows=[]
    for name,title,desc,t in svg_items():
        vb=[float(x) for x in re.search(r'viewBox="([^"]*)"',t).group(1).split()]; wide=' class="wide"' if vb[2]/vb[3]>3 else ''
        rows.append(f'      <li><div class="sv-f"><img{wide} alt="{html.escape(title)}" src="data:image/svg+xml;base64,{base64.b64encode(t.encode()).decode()}"></div><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p><p><code>{name}</code></p><div class="sv-b"><button class="sv-re" type="button">Replay</button><button class="copy" type="button">Copy SVG</button><pre hidden>{html.escape(t)}</pre></div></li>')
    return '\n'.join(rows)
def facet_macro(m):
    f,on=m.group(1).split()
    return ''.join(f'<label><input type="radio" name="pk-{f}" value="{k}"{" checked" if k==on else ""}><span>{html.escape(v)}</span></label>' for k,v in C.FACETS[f])
def pick_macro(m):
    g,a,f=m.group(1).split(); rows=[]
    for r in C.recommend(g,a,f):
        files=' '.join(f'<code>base/templates/{x}</code>' for x in r['files'])
        rows.append(f'<li><h3>{html.escape(r["title"])}</h3><p class="pk-w">{html.escape(r["why"])}</p><p class="pk-l"><b>Look:</b> {html.escape(r["look"])}. <b>Files:</b> {files}</p><div class="ask"><h3>Ask for it like this</h3><blockquote>{html.escape(r["ask"])}</blockquote><button class="copy" type="button">Copy</button></div></li>')
    return '\n'.join(rows)
def md_macro(m): return '<article class="md sub"><div class="wrap">'+md_html(os.path.normpath(os.path.join(ROOT,m.group(1).strip())),drop_h1=True)+'</div></article>'
def md_view(name,title,path,raw=None):
    if raw: inner=f'<h1>{html.escape(title)}</h1><p>{raw}</p><div class="codeb"><pre>{html.escape(re.sub(r"^<!--.*?-->\s*","",open(path).read(),flags=re.S).strip())}</pre><button class="copy" type="button">Copy</button></div>'
    else: inner=md_html(path)
    return f'<div class="view" id="v-{name}" data-title="{html.escape(title)}"><article class="md"><div class="wrap">{inner}</div></article></div>'

# every view file: css always, script and markup kept by name
css=[];VIEW={};VJS={};LIB=[];LV={};VCSS={};VFILE={}
for f in sorted(glob.glob(os.path.join(HERE,'views','*.html'))):
    t=open(f).read()
    own=[m.group(1).strip() for m in re.finditer(r'<style>(.*?)</style>',t,re.S)]; css+=own
    sc=[m.group(1).strip() for m in re.finditer(r'<script>(.*?)</script>',t,re.S)]
    t=re.sub(r'<style>.*?</style>|<script>.*?</script>','',t,flags=re.S).strip()
    lvm=re.search(r'^@@levels (.*)$',t,re.M)
    t=re.sub(r'^@@ask (.*)$',ask_macro,t,flags=re.M); t=re.sub(r'^@@levels (.*)$',levels_macro,t,flags=re.M); t=re.sub(r'^\s*@@md (.*)$',md_macro,t,flags=re.M)
    t=re.sub(r'^@@svgset$',svgset_macro,t,flags=re.M); t=re.sub(r'^@@facet (.*)$',facet_macro,t,flags=re.M); t=re.sub(r'^@@pick (.*)$',pick_macro,t,flags=re.M)
    m=re.search(r'id="v-([\w-]+)"',t)
    if m and lvm: LV[m.group(1)]=[x.strip() for x in lvm.group(1).split('||')]
    if not m: LIB+=sc; continue
    VFILE[m.group(1)]=os.path.basename(f); VIEW[m.group(1)]=t; VJS[m.group(1)]=sc; VCSS[m.group(1)]='\n'.join(own)
# level 1's instructions for the assistant are the single-file skill without its header, written first so the tab below can show them
_one=open(os.path.join(SKILL,'SKILL-single-file.md')).read().split('---',2)[2].strip()
open(os.path.join(ROOT,'level-1','AI-INSTRUCTIONS.md'),'w').write('<!-- Generated from skills/artifact-studio/SKILL-single-file.md by base/source/build.py. Edit that file, not this one. -->\n\n'+_one+'\n')
MD={ # name: (title, path, note shown above a copy-ready block or None to render the Markdown)
 'c-recipes':('Recipe cards',SKILL+'/references/recipes.md',None),
 'c-voices':('Voice cards',SKILL+'/references/voices.md',None),
 'c-parts':('Parts list',SKILL+'/references/components.md',None),
 'c-spec':('Design spec',ROOT+'/base/forms/design-spec.md','Your colours and type on one page. Fill it in once and attach it to a request, or paste it into your preferences file at level 2. Copy it, then replace the parts in brackets.'),
 'c-brief':('Content brief',ROOT+'/base/forms/content-brief.md','Fill this in for each page. Five lines that tell the assistant who the page is for and what it must do. Copy it, then replace the parts in brackets.'),
 'c-sentences':('All sentences',ROOT+'/base/sentences.md',None),
 's-skill':('The skill',SKILL+'/SKILL.md',None),
 's-single':('AI instructions',ROOT+'/level-1/AI-INSTRUCTIONS.md','Level 1 needs only this. It is the whole skill in one file. Copy it and paste it into the instructions of a Project, or into the first message of a chat.'),
 's-skel':('Page skeleton',SKILL+'/assets/page-skeleton.html','The starting file the skill builds from. One self-contained page with the tokens, the type scale and the motion rules already in place.'),
 's-rules':('Build rules',SKILL+'/references/build-rules.md',None),
 's-check':('Checklist',SKILL+'/references/pre-ship-checklist.md',None),
  's-best':('Best practices',ROOT+'/base/BEST-PRACTICES.md',None)}
for n,(title,path,raw) in MD.items(): VIEW[n]=md_view(n,title,path,raw); VJS[n]=[]
LABEL={'voice-keynote':'Keynote','voice-story':'Storyteller','voice-teacher':'Teacher','voice-pitch':'Pitch','voice-practical':'Practical','voice-analyst':'Analyst','voice-brief':'Brief',
       'recipe-report':'Report','recipe-proposal':'Proposal','recipe-explainer':'Explainer','recipe-landing':'Landing page'}
VOICES=['voice-keynote','voice-story','voice-teacher','voice-pitch','voice-practical','voice-analyst','voice-brief']
RECIPES=['recipe-report','recipe-proposal','recipe-explainer','recipe-landing']
G_VOICES=('Voices',VOICES,'One message, told seven ways. Tap a voice:'); G_RECIPES=('Recipes',RECIPES,'Four whole pages. Tap a recipe:')
STUDIO_GROUPS=[G_VOICES,('Pages',RECIPES,'Four whole pages. Tap one:'),('Decks',['deck-visionary','deck-story'],'Two slide decks on one engine:'),('Social',['social'],''),
  ('Parts',['parts','photo','svg','looks'],'The pieces a page is made of:'),('Pick',['pick','mix'],'Let the studio suggest, or choose every part yourself:'),
  ('Cards',['c-recipes','c-voices','c-parts','c-spec','c-brief','c-sentences'],'The reference cards, the two forms and every sentence:'),
  ('Skill',['s-skill','s-single','s-skel','s-rules','s-check','s-best'],'What the assistant follows. "AI instructions" is the paste-in version:'),
  ('Guide',['use'],'')]
LABEL.update({'parts':'Page parts','photo':'Photo parts','svg':'Animated SVG','looks':'Looks','pick':'Pick for me','mix':'Mix it myself','deck-visionary':'Visionary','deck-story':'Story'})
# every template again as a file of its own: view -> (file under base/templates, title)
FILES={t['id']:t['file'].split('#')[0] for t in C.TEMPLATES if t['kind'] in('page','voice','deck')}
FILES.update({'social':'social/formats.html','parts':'components/page-parts.html','photo':'components/photo-parts.html','svg':'components/animated-svg.html','looks':'looks/nine-looks.html'})
FTITLE={'social':'Seven social formats','parts':'Twelve page parts','photo':'Twelve photo parts','svg':'Twelve animated SVG parts','looks':'Nine looks'}
FTITLE.update({t['id']:t['title'] for t in C.TEMPLATES})
TAB={t['id']:(t['id'] if t['kind']!='social' else 'social') for t in C.TEMPLATES}
# a short "about" strip at the top of every voice and recipe tab, taken from the voice cards and from the page's own closing note
_v=open(SKILL+'/references/voices.md').read()
_use={n.strip():u.strip() for u,n in re.findall(r'^\| ([^|]+) \| ([^|]+) \|$',_v[_v.index('## Choosing'):_v.index('## Keynote')],re.M) if n.strip() not in ('Use','---')}
_by=dict(re.findall(r'^## ([^\n]+)\n\n\| Field \| \|\n\| --- \| --- \|\n\| Inspired by \| ([^|]+) \|',_v,re.M))
VNAME={'voice-keynote':'Keynote','voice-story':'Storyteller','voice-teacher':'Teacher','voice-pitch':'Pitch','voice-practical':'Practical instructor','voice-analyst':'Analyst','voice-brief':'Executive brief'}
def about(n,t,key='all'):
    if n in VNAME:
        k=VNAME[n]; u=_use[k]; by=_by[k].strip(); by=by[0].lower()+by[1:] if by.startswith(('The ','A ')) else by; txt=f'<b>The {k.lower()} voice.</b> Inspired by {html.escape(by)}. Use it when the reader should {u[0].lower()+u[1:]}.'
        note='A full example follows.'
    elif n.startswith('recipe-'):
        m=re.search(r'<section class="anat">.*?<p class="measure">(.*?)</p>',t,re.S); first=re.split(r'(?<=\.) ',m.group(1).strip())[0]
        txt=f'<b>The {re.search(chr(100)+'ata-title="([^"]*)"',t).group(1).lower()} recipe.</b> {first}'; note='A full example follows, with invented content.'
    else: return t
    i={'beginner':0,'advanced':1}.get(key); ask=''
    if i is not None and n in LV: ask=f'<div class="ask"><h3>{("Beginner","Advanced")[i]}: ask for it like this</h3><blockquote>{LV[n][i]}</blockquote><button class="copy" type="button">Copy</button></div>'
    if ask and i==1: ask='<details class="about-d"><summary>Show the advanced request that asks for this page</summary>'+ask.replace('<h3>Advanced: ask for it like this</h3>','<h3>Paste it with your brief and notes</h3>')+'</details>'
    strip=f'<aside class="about" aria-label="About this example"><div class="wrap"><p>{txt}</p>{ask}<p class="about-n">{note} <a href="#anat-{n}" data-jump="anat-{n}">How it is built{"" if ask else ", and the sentence that asks for it"}</a></p></div></aside>'
    t=t.replace('<section class="anat">',f'<section class="anat" id="anat-{n}">',1)
    return re.sub(r'(<div class="view"[^>]*>)',lambda m:m.group(1)+strip,t,count=1)
SHELL=open(os.path.join(HERE,'shell.html')).read()
BASE=open(os.path.join(HERE,'base.css')).read()
PAGE_INDEX={'templates':[dict(t,tab=TAB[t['id']]) for t in C.TEMPLATES],'rules':C.RULES,'labels':{f:dict(v) for f,v in C.FACETS.items()}}
data=json.dumps({'rows':A['rows'],'pal':A['pal'],'index':PAGE_INDEX},separators=(',',':'))
def title_of(n): return LABEL.get(n) or re.search(r'data-title="([^"]*)"',VIEW[n]).group(1)
PREFIX={}
def build(key,out,title,lead,groups):
    single=len(groups)==1 and len(groups[0][1])==1
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
    if single: radios=[]; nav=''; tcss=[f'#v-{order[0]}{{display:block}}','.mast{padding-bottom:14px}']
    mast=f'<header class="mast"><div class="wrap"><p class="mast-t"><span>{PREFIX.get(key,"Artifact studio template") if single else "Artifact studio"}</span> {html.escape(title)}</p><p class="mast-l">{html.escape(lead)}</p></div></header>'
    body=[]
    for k,n in enumerate(order):
        t=about(n,VIEW[n],key); prev=order[k-1] if k else None; nxt=order[k+1] if k+1<len(order) else None
        pager='<nav class="pager" aria-label="Previous and next tab"><div>'+(f'<label for="t-{prev}">← {html.escape(title_of(prev))}</label>' if prev else '<span></span>')+(f'<label for="t-{nxt}">{html.escape(title_of(nxt))} →</label>' if nxt else '<span></span>')+'</div></nav>'
        body.append(t if single else t[:t.rindex('</div>')]+pager+'</div>')
    js=LIB+[x for n in order for x in VJS[n]]
    js='\n'.join('<script>\ntry{(()=>{\n'+x+'\n})()}catch(err){console.error(err)}\n</script>' for x in js)
    mk='\n'.join(VIEW[n] for n in order); vc='\n'.join(VCSS.get(n,'')+'\n'.join(VJS.get(n,[])) for n in order)
    p1=(not single) or 'photo' in order or bool(re.search(r'class="(?![^"]*\bph2\b)[^"]*\bph\b',mk)) or 'var(--photo)' in vc or 'data-crop' in mk
    p2=(not single) or 'photo' in order or 'ph2' in mk or '--photo2' in vc
    if single and order[0] in ('voice-keynote','voice-story'): p1=False          # these two repaint every photo frame with the second photograph
    photos=(f'--photo:url("data:image/jpeg;base64,{A["photo"]}");' if p1 else '')+(f'--photo2:url("data:image/jpeg;base64,{A["sunset"]}");' if p2 else '')
    t=SHELL.replace('<title>Artifact studio</title>',f'<title>Artifact studio: {html.escape(title)}</title>' if title else '<title>Artifact studio</title>')
    t=t.replace('/*FONTS*/',fonts).replace('/*PHOTOS*/',photos).replace('/*BASE_CSS*/',BASE).replace('/*TAB_CSS*/','\n'.join(tcss)).replace('/*VIEW_CSS*/','\n'.join(css))
    t=t.replace('<!--MAST-->',mast).replace('<!--RADIOS-->','\n'.join(radios)).replace('<!--NAV-->',nav).replace('<!--VIEWS-->','\n'.join(body)).replace('<!--VIEW_JS-->',js)
    t=t.replace('__PATHS__',paths).replace('__DATA__',data).replace('__TOPHEX__',A['pal'][0]['hex']).replace('__TOPSHARE__',str(round(A['pal'][0]['share'])))
    kb=round(len(t.encode())/1024); t=t.replace('__KB__',f'{kb:,}')
    left=re.findall(r'__[A-Z]+__|^\s*@@\w+',re.sub(r'data:[^")]+','',re.sub(r'<pre>.*?</pre>','',t,flags=re.S)),flags=re.M); assert not left, left
    open(os.path.join(ROOT,out),'w').write(t); print(f'{key}: {kb} KB, {len(order)} tabs -> {out}')
build('studio','base/studio.html','','Everything in one page: voices, pages, decks, social formats and parts, then a picker, the cards, the skill and a guide. Tap a tab.',STUDIO_GROUPS)
for n,fn in FILES.items():
    os.makedirs(os.path.dirname(os.path.join(ROOT,'base','templates',fn)),exist_ok=True)
    build(n,'base/templates/'+fn,FTITLE[n],'A complete template in one file. Copy it as a starting point, or ask for one like it with the sentence at the end.',[(FTITLE[n],[n],'')])

# ---- reports: any Markdown file in docs/reports becomes a page in the same style
REPO=os.path.normpath(os.path.join(ROOT,'..','..'))
for f in sorted(glob.glob(os.path.join(REPO,'docs','reports','*.md'))):
    key='report-'+os.path.basename(f)[:-3]; src=open(f).read(); ttl=re.search(r'^# (.+)$',src,re.M).group(1)
    VIEW[key]=f'<div class="view" id="v-{key}" data-title="{html.escape(ttl)}"><article class="md"><div class="wrap">{md_html(f,drop_h1=True)}</div></article></div>'; VJS[key]=[]; PREFIX[key]='Practical AI report'
    build(key,os.path.relpath(f[:-3]+'.html',ROOT),ttl,'What was proposed, what was built, how to use it, and what has not been checked.',[(ttl,[key],'')])

# ---- the index: one machine-readable file and one page for people, both generated, so neither can drift from the templates
def write_index(parts,photo):
    import datetime
    slug=lambda x: re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-')
    T='base/templates/'; looks=re.findall(r'^## (.+)$',open(SKILL+'/references/looks.md').read(),re.M)
    looks=[l for l in looks if l in ('Clean','Cinematic','Scrollytelling','Dashboard','Editorial','Keynote black','Paper memo','Field guide','Faded film')]
    tpl=[]
    for t in C.TEMPLATES:
        view=TAB[t['id']]; lv=LV.get(t['id'])
        ask={'short':lv[0],'full':lv[1],'with_skill':lv[2]} if lv else {'short':t['ask']}
        e=dict(id=t['id'],kind=t['kind'],title=t['title'],summary=t['summary'],file=T+t['file'],source='base/source/views/'+VFILE[view],fit=t['fit'],options=C.OPTIONS[t['kind']],ask=ask)
        for k in('look','size','voice'):
            if k in t: e[k]=t[k]
        if t['kind']=='voice': e['default_look']=C.RULES['look_for_voice'][t['id']]
        tpl.append(e)
    comp=[dict(id='page-'+slug(n),group='page',name=n,use=use.rstrip('.'),ask=q,effort=effort,file=T+'components/page-parts.html',source='base/source/views/30-parts.html') for n,blurb,q,effort,made,grow,use in parts]
    comp+=[dict(id='photo-'+slug(n),group='photo',name=n,use=blurb,ask=q,effort=effort,file=T+'components/photo-parts.html',source='base/source/views/20-photo.html') for n,blurb,q,effort,made,grow,use in photo]
    comp+=[dict(id='svg-'+name[:-4],group='svg',name=title,use=desc,ask=f'Add the "{name[:-4]}" animated SVG from the artifact studio, recoloured to my accent colour.',effort='Copy one file',file=T+'components/svg/'+name,source=T+'components/svg/'+name) for name,title,desc,_ in svg_items()]
    for c in comp:
        g=T+'components/gif/'+os.path.basename(c['file'])[:-4]+'.gif'
        if c['group']=='svg' and os.path.exists(os.path.join(ROOT,g)): c['gif']=g
    kinds=['page','voice','deck','social']
    counts={'templates':len(tpl),**{k+'s' if k!='social' else 'social_formats':sum(t['kind']==k for t in tpl) for k in kinds},'components':len(comp),'page_parts':len(parts),'photo_parts':len(photo),'animated_svg':sum(c['group']=='svg' for c in comp),'gif_copies':sum('gif' in c for c in comp),'looks':len(looks)}
    idx=dict(name='artifact-studio',generated=datetime.date.today().isoformat(),
             read_me='Paths are relative to drafts/artifact-studio/. "file" is the finished template to open or copy. "source" is the smaller file to read as reference code: one style block, the markup and one script. "fit" scores run 0 to 3. To choose, score = 3 x goal fit + 2 x audience fit, highest first.',
             counts=counts,facets={f:[dict(id=k,label=v) for k,v in v2] for f,v2 in C.FACETS.items()},rules=C.RULES,templates=tpl,components=comp,
             looks=[dict(name=l,file=T+'looks/nine-looks.html',card='skills/artifact-studio/references/looks.md') for l in looks])
    json.dump(idx,open(os.path.join(ROOT,'base','templates','index.json'),'w'),indent=1)
    rel=lambda p:p.replace(T,'')
    o=['# Templates','','Everything the studio can make, in one index. Open a file to see it, copy it to start from it, or give the short ask to an assistant.','',
       'This page and [`index.json`](index.json) are generated by `base/source/build.py` from the templates themselves. Edit the views or `base/source/catalog.py`, not this file.','',
       f"**In the library:** {counts['templates']} templates ({counts['pages']} pages, {counts['voices']} voices, {counts['decks']} decks, {counts['social_formats']} social formats), {counts['components']} components ({counts['page_parts']} page parts, {counts['photo_parts']} photo parts, {counts['animated_svg']} animated SVG files) and {counts['looks']} looks.",'',
       '| Folder | What is in it |','| --- | --- |','| [`pages/`](pages/) | Whole pages: report, proposal, explainer, landing page |','| [`voices/`](voices/) | One case told seven ways, each a full page |','| [`decks/`](decks/) | Slide decks you present with the arrow keys |','| [`social/`](social/) | Post shapes you download as pictures |','| [`components/`](components/) | The parts: page parts, photo parts and animated SVG files |','| [`looks/`](looks/) | One line dressed nine ways |','',
       'Every example uses invented content. GitHub shows HTML as source, so download a file and open it in a browser.','']
    for k,head,note in (('page','Pages','A page is the structure. Pair it with a voice.'),('voice','Voices','A voice is how the piece speaks. All seven tell the same invented case.'),('deck','Decks','One deck engine, two manners. Each is a single file.'),('social','Social formats','All seven pictures are in one file, with download buttons.')):
        o+=[f'## {head}','',note,'','**What you can change:** '+C.OPTIONS[k],'','| Template | Use it when you need to | Open | Short ask |','| --- | --- | --- | --- |']
        for t in tpl:
            if t['kind']!=k: continue
            best=[dict(C.FACETS['goal'])[g].lower() for g,v in sorted(t['fit']['goal'].items(),key=lambda x:-x[1]) if v>=2]
            o.append(f"| **{t['title']}**. {t['summary']} | {', '.join(best) or 'see the summary'} | [`{rel(t['file']).split('#')[0]}`]({rel(t['file']).split('#')[0]}) | {t['ask']['short']} |")
        o.append('')
    for g,head,f in (('page','Page parts','components/page-parts.html'),('photo','Photo parts','components/photo-parts.html')):
        o+=[f'## {head}','',f'All twelve are in [`{f}`]({f}), each with the sentence that asks for it.','','| Part | Use it for |','| --- | --- |']+[f"| {c['name']} | {c['use']} |" for c in comp if c['group']==g]+['']
    o+=['## Animated SVG','','Each is one file with no script. See them move in [`components/animated-svg.html`](components/animated-svg.html).','','Where SVG is not accepted, such as email and some slide tools, use the GIF copy. The GIFs are made from the SVG files by `base/source/svg_to_gif.py`.','','| File | GIF copy | What it is | Use |','| --- | --- | --- | --- |']
    o+=[f"| [`{os.path.basename(c['file'])}`]({rel(c['file'])}) | "+(f"[`gif`]({rel(c['gif'])})" if 'gif' in c else 'none')+f" | {c['name']} | {c['use']} |" for c in comp if c['group']=='svg']
    o+=['','## Looks','','Nine looks, shown side by side in [`looks/nine-looks.html`](looks/nine-looks.html): '+', '.join(looks)+'. The cards are in the skill.','',
        '## How a combination is picked','','Each template carries a score from 0 to 3 for six goals and five audiences. A request is scored as three times the goal fit plus twice the audience fit, and the highest wins. The scores are in [`index.json`](index.json) and `base/source/catalog.py`, so you can read them and change them. The Pick tab of the studio page and the MCP server both use the same rules.','']
    open(os.path.join(ROOT,'base','templates','README.md'),'w').write('\n'.join(o))
    line=f"{counts['templates']} templates ({counts['pages']} pages, {counts['voices']} voices, {counts['decks']} decks, {counts['social_formats']} social formats), {counts['components']} components ({counts['page_parts']} page parts, {counts['photo_parts']} photo parts, {counts['animated_svg']} animated SVG files with {counts['gif_copies']} GIF copies) and {counts['looks']} looks"
    for readme in (os.path.join(ROOT,'README.md'),os.path.join(ROOT,'base','README.md')):
        t=open(readme).read(); t2=re.sub(r'<!-- counts -->.*?<!-- /counts -->',f'<!-- counts -->{line}<!-- /counts -->',t,flags=re.S)
        if t2!=t: open(readme,'w').write(t2)
    print('index:',counts)

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
        kind='voice' if 'voice-' in f else 'recipe' if 'recipe-' in f else 'deck' if 'deck-' in f else 'more'
        lv.append((kind,title,about,[x.strip() for x in m.group(1).split('||')]))
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
       'This file is generated from the examples by `base/source/build.py`. Edit the views, not this file.','']
    for kind,head in (('recipe','Pages'),('voice','Voices'),('deck','Decks'),('more','Social formats and animated SVG')):
        o+=[f'## {head}','']
        for k,title,about,(b,a,e) in lv:
            if k!=kind: continue
            o+=[f'### {title}','',about,'',f'- **Short ask:** {b}',f'- **Full ask:** {a}',f'- **With the skill:** {e}','']
    for head,rows,last in (('Page components',parts,'Use it for'),('Photo components',photo,'Seen in')):
        o+=[f'## {head}','']
        for name,blurb,q,effort,made,grow,use in rows:
            if name=='Looks and voices':
                o+=[f'### {name}','',blurb,'']+[f'- **{n}:** {a}' for i,n,line,voice,by,a in looks]+['']; continue
            o+=[f'### {name}','',blurb,'',f'> {q}','',f'Effort: {effort} {last}: {use.rstrip(".")}.','']
    open(os.path.join(ROOT,'base','sentences.md'),'w').write('\n'.join(o).rstrip()+'\n')
    c=['# Component catalogue','','The parts a page can be built from. Each row is a working example in the studio. Pick parts that carry content; never add one for decoration.','',
       'Generated from the examples by `drafts/artifact-studio/base/source/build.py`.','']
    for head,rows in (('Page components (no photo needed)',parts),('Photo components',photo)):
        c+=[f'## {head}','','| Component | What it is for | How it is made | Grow into |','| --- | --- | --- | --- |']
        c+=[f'| {n} | {b} | {made} | {grow} |' for n,b,q,effort,made,grow,use in rows]+['']
    sk=os.path.join(HERE,'..','..','..','..','skills','artifact-studio','references','components.md')
    write_index(parts,photo)
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
