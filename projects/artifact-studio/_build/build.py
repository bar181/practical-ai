"""build.py: rebuild everything the artifact studio generates, from one catalogue and a folder of views.

Reads   catalog.py (templates, fit scores, social styles, the palette rule), shell.html, base.css, assets.json,
        views/*.html, svg/*.svg, forms/*.md and the skill's Markdown files in ../level-2-files/artifact-studio/
Writes  ../base/studio.html                                  every view as a tab
        ../base/AI-INSTRUCTIONS.md                           a copy of the skill's single-file edition
        ../level-2-files/artifact-studio/assets/starters/    each deck and social picture as one small file
        ../level-2-files/artifact-studio/references/         components.md and design-ideas.md
        ../level-3-files/mcp/catalog.py and library/         what the MCP server reads: the index, the template sources, the SVG parts
        sentences.md                                         every ask, in one list (shown as a tab)
        the counts line in ../README.md

A view is one file: an optional <style>, the markup (a div.view with id v-NAME), and an optional <script> that
registers onView("NAME", root => { ... }) to run the first time the view is shown.
Macros, each on a line of its own:
  @@ask sentence || effort || made here with || grow into || use it for      the ask box under a part
  @@levels short ask || full ask || ask with the skill                         the three asks under a template
  @@md path    @@svgset    @@facet name default    @@pick goal audience format    @@palette hue

Run: python3 build.py   (prepare_assets.py is needed only when a font or photograph changes)
This file is dense. The tests that covered it are in the repository's history, before the project was simplified.
"""
import json, os, re, glob, html
import shutil
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
ROOT=os.path.normpath(os.path.join(HERE,'..'))                 # the project folder
SKILL=os.path.join(ROOT,'level-2-files','artifact-studio'); LIBRARY=os.path.join(ROOT,'level-3-files','mcp','library')
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
SVGDIR=os.path.join(HERE,'svg')
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
        rows.append(f'<li><h3>{html.escape(r["title"])}</h3><p class="pk-w"><b class="pk-s {r["strength"]}">{r["strength"].capitalize()} fit.</b> {html.escape((r["note"]+" ") if r["note"] else "")}{html.escape(r["why"])}</p><p class="pk-l"><b>Look:</b> {html.escape(r["look"])}.</p><div class="ask"><h3>Ask for it like this</h3><blockquote>{html.escape(r["ask"])}</blockquote><button class="copy" type="button">Copy</button></div></li>')
    return '\n'.join(rows)
def palette_html(p):
    sw=''.join(f'<li><i style="background:{r["hex"]}"></i><b>{html.escape(r["use"])}</b><code>{r["hex"]}</code></li>' for r in p['roles'])
    ck=''.join(f'<li class="{"ok" if k["passes"] else "no"}"><b>{k["ratio"]:.1f} to 1</b> {html.escape(k["pair"])} <span>needs {k["needs"]:g}</span></li>' for k in p['checks'])
    spec='Colours, from hue '+str(p['hue'])+'\n'+'\n'.join(f'- {r["use"]}: {r["hex"]}' for r in p['roles'])+'\n- Rule: '+p['rule']
    col={r['id']:r['hex'] for r in p['roles']}
    mock=(f'<div class="co-mock" style="background:{col["surface"]};color:{col["ink"]};border-color:{col["line"]}"><b>Your headline goes here</b><p style="color:{col["muted"]}">Secondary text sits quietly beside it.</p>'
          f'<div class="co-panel" style="background:{col["surface2"]};border-color:{col["line"]}"><mark style="background:{col["accentsoft"]};color:{col["ink"]}">A highlight</mark> inside a panel.</div><span class="co-btn" style="background:{col["accent"]}">The one action</span></div>')
    return f'<div class="co-out">{mock}<ul class="co-sw">{sw}</ul><ul class="co-ck">{ck}</ul><div class="ask co-spec"><h3>Paste this into your design spec</h3><blockquote>{html.escape(spec)}</blockquote><button class="copy" type="button">Copy</button></div></div>'
def palette_macro(m): return palette_html(C.palette(int(m.group(1))))
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
    t=re.sub(r'^@@svgset$',svgset_macro,t,flags=re.M); t=re.sub(r'^@@facet (.*)$',facet_macro,t,flags=re.M); t=re.sub(r'^@@pick (.*)$',pick_macro,t,flags=re.M); t=re.sub(r'^@@palette (\d+)$',palette_macro,t,flags=re.M)
    m=re.search(r'id="v-([\w-]+)"',t)
    if m and lvm: LV[m.group(1)]=[x.strip() for x in lvm.group(1).split('||')]
    if not m: LIB+=sc; continue
    VFILE[m.group(1)]=os.path.basename(f); VIEW[m.group(1)]=t; VJS[m.group(1)]=sc; VCSS[m.group(1)]='\n'.join(own)
# level 1's instructions for the assistant are the single-file skill without its header, written first so the tab below can show them
_one=open(os.path.join(SKILL,'SKILL-single-file.md')).read().split('---',2)[2].strip()
open(os.path.join(ROOT,'base','AI-INSTRUCTIONS.md'),'w').write('<!-- Generated from level-2-files/artifact-studio/SKILL-single-file.md by _build/build.py. Edit that file, not this one. -->\n\n'+_one+'\n')
MD={ # name: (title, path, note shown above a copy-ready block or None to render the Markdown)
 'c-recipes':('Recipe cards',SKILL+'/references/recipes.md',None),
 'c-voices':('Voice cards',SKILL+'/references/voices.md',None),
 'c-parts':('Parts list',SKILL+'/references/components.md',None),
 'c-spec':('Design spec',HERE+'/forms/design-spec.md','Your colours and type on one page. Fill it in once and attach it to a request, or paste it into your preferences file at level 2. Copy it, then replace the parts in brackets.'),
 'c-brief':('Content brief',HERE+'/forms/content-brief.md','Fill this in for each page. Five lines that tell the assistant who the page is for and what it must do. Copy it, then replace the parts in brackets.'),
 'c-sentences':('All sentences',HERE+'/sentences.md',None),
 's-skill':('The skill',SKILL+'/SKILL.md',None),
 's-single':('AI instructions',ROOT+'/base/AI-INSTRUCTIONS.md','Level 1 needs only this. It is the whole skill in one file. Copy it and paste it into the instructions of a Project, or into the first message of a chat.'),
 's-skel':('Page skeleton',SKILL+'/assets/page-skeleton.html','The starting file the skill builds from. One self-contained page with the tokens, the type scale and the motion rules already in place.'),
 's-rules':('Build rules',SKILL+'/references/build-rules.md',None),
 's-check':('Checklist',SKILL+'/references/pre-ship-checklist.md',None)}
for n,(title,path,raw) in MD.items(): VIEW[n]=md_view(n,title,path,raw); VJS[n]=[]
LABEL={'voice-keynote':'Visionary','voice-story':'Storyteller','voice-teacher':'Explainer','voice-practical':'Practical','voice-analyst':'Analyst','voice-brief':'Brief',
       'recipe-report':'Report','recipe-proposal':'Proposal','recipe-explainer':'Explainer','recipe-landing':'Landing page'}
VOICES=['voice-keynote','voice-story','voice-teacher','voice-practical','voice-analyst','voice-brief']
RECIPES=['recipe-report','recipe-proposal','recipe-explainer','recipe-landing']
CONCEPTS=(('card','31-cards.html','components/cards.html','Cards'),('layout','32-layouts.html','components/layouts.html','Layouts'),('colour','33-colour.html','components/colour.html','Colour'))
G_VOICES=('Voices',VOICES,'One message, told six ways. Tap a voice:'); G_RECIPES=('Recipes',RECIPES,'Four whole pages. Tap a recipe:')
# two files. Highlights: the photo and scroll effects, the looks and layouts, and one tab for each voice. Components: everything else.
POSTS=['post-linkedin','post-instagram','post-tiktok','post-facebook','post-email','post-blog']
HIGHLIGHT_GROUPS=[('Photo effects',['photo'],''),('Scroll effects',['scroll'],''),('Layouts',['lookvoice','looks','layouts'],'Looks set the mood and layouts set the order:'),('Socials',['socials'],'')]+[(LABEL[v],[v],'') for v in VOICES]
COMPONENT_GROUPS=[('Pages',RECIPES,'Four whole pages. Tap one:'),('Decks',['deck-visionary','deck-story','deck-briefing','deck-workshop'],'Four slide decks on one engine:'),('Socials',POSTS+['social'],'See each draft the way your audience will. Tap a platform:'),
  ('Parts',['parts','svg'],'The pieces a page is made of:'),('Design',['cards','colour'],'The ideas behind a good page:'),('Pick',['pick','mix'],'Let the studio suggest, or choose every part yourself:'),
  ('Reference',['c-recipes','c-voices','c-parts','c-spec','c-brief','c-sentences'],'The reference sheets, the two forms and every sentence:'),
  ('Skill',['s-skill','s-single','s-skel','s-rules','s-check'],'What the assistant follows. "AI instructions" is the paste-in version:'),
  ('Guide',['use'],'')]
OUT={'highlights':'base/studio.html','components':'base/components.html'}
WHERE={n:OUT[k] for k,gs in (('highlights',HIGHLIGHT_GROUPS),('components',COMPONENT_GROUPS)) for _,vs,_ in gs for n in vs}   # which file shows each tab
pv=lambda view: WHERE[view]+'#'+view
LABEL.update({'socials':'Socials','post-linkedin':'LinkedIn','post-instagram':'Instagram','post-tiktok':'TikTok','post-facebook':'Facebook','post-email':'Email','post-blog':'Short blog','social':'Picture formats','cards':'Cards','layouts':'Six layouts','colour':'Colour','parts':'Page parts','photo':'Photo effects','scroll':'Scroll effects','lookvoice':'Looks and voices','svg':'Animated SVG','looks':'Nine looks','pick':'Pick for me','mix':'Mix it myself','deck-visionary':'Visionary','deck-story':'Story','deck-briefing':'Briefing','deck-workshop':'Workshop'})
FILES={t['id']:t['file'].split('#')[0] for t in C.TEMPLATES if t['kind'] in('page','voice','deck')}
FILES.update({'cards':'components/cards.html','layouts':'components/layouts.html','colour':'components/colour.html','social':'social/formats.html','parts':'components/page-parts.html','photo':'components/photo-parts.html','svg':'components/animated-svg.html','looks':'looks/nine-looks.html'})
FTITLE={'cards':'Six kinds of card','layouts':'Six layouts','colour':'Colour: five ideas and a palette maker','social':'Seven social formats','parts':'Twelve page parts','photo':'Nine photo effects','scroll':'Three scroll effects','lookvoice':'Looks and voices','svg':'Twelve animated SVG parts','looks':'Nine looks'}
FTITLE.update({t['id']:t['title'] for t in C.TEMPLATES})
TAB={t['id']:(t['id'] if t['kind']!='social' else 'social') for t in C.TEMPLATES}
# a short "about" strip at the top of every voice and recipe tab, taken from the voice cards and from the page's own closing note
_v=open(SKILL+'/references/voices.md').read()
_use={n.strip():u.strip() for u,n in re.findall(r'^\| ([^|]+) \| ([^|]+) \|$',_v[_v.index('## Choosing'):_v.index('## Keynote')],re.M) if n.strip() not in ('Use','---')}
_by=dict(re.findall(r'^## ([^\n]+)\n\n\| Field \| \|\n\| --- \| --- \|\n\| Inspired by \| ([^|]+) \|',_v,re.M))
VNAME={'voice-keynote':'Keynote','voice-story':'Storyteller','voice-teacher':'Teacher','voice-practical':'Practical instructor','voice-analyst':'Analyst','voice-brief':'Executive brief'}
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
# pictures beyond the two in assets.json: each file in photos/ named here becomes a CSS variable, --ph-NAME
EXTRA={k:f'--ph-{k}:url("data:image/jpeg;base64,{base64.b64encode(open(os.path.join(HERE,"photos",k+".jpg"),"rb").read()).decode()}");' for k in ('toronto','dog','puzzle','class','fog','bulb','cat','home')}
SHELL=open(os.path.join(HERE,'shell.html')).read()
BASE=open(os.path.join(HERE,'base.css')).read()
PAGE_INDEX={'templates':[dict(t,tab=TAB[t['id']]) for t in C.TEMPLATES],'rules':C.RULES,'labels':{f:dict(v) for f,v in C.FACETS.items()},'social_styles':C.SOCIAL_STYLES,'palette_roles':C.PALETTE_ROLES,'palette_rule':C.palette(0)['rule']}
data=json.dumps({'rows':A['rows'],'pal':A['pal'],'index':PAGE_INDEX},separators=(',',':'))
def title_of(n): return LABEL.get(n) or re.search(r'data-title="([^"]*)"',VIEW[n]).group(1)
PREFIX={}
def build(key,out,title,lead,groups,other=None):
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
    here=os.path.basename(out); elsewhere={n:os.path.basename(f) for n,f in WHERE.items() if os.path.basename(f)!=here and n not in order}
    mast_x=f'<p class="mast-x"><a href="{other[0]}">{html.escape(other[1])}</a></p>' if other else ''
    mast=f'<header class="mast"><div class="wrap"><p class="mast-t"><span>{PREFIX.get(key,"Artifact studio template") if single else "Artifact studio"}</span> {html.escape(title)}</p><p class="mast-l">{html.escape(lead)}</p>{mast_x}</div></header>'
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
    photos=(f'--photo:url("data:image/jpeg;base64,{A["photo"]}");' if p1 else '')+(f'--photo2:url("data:image/jpeg;base64,{A["sunset"]}");' if p2 else '')+''.join(v for k,v in EXTRA.items() if f'--ph-{k}' in vc+mk)
    t=SHELL.replace('<title>Artifact studio</title>',f'<title>Artifact studio: {html.escape(title)}</title>' if title else '<title>Artifact studio</title>')
    t=t.replace('/*FONTS*/',fonts).replace('/*PHOTOS*/',photos).replace('/*BASE_CSS*/',BASE).replace('/*TAB_CSS*/','\n'.join(tcss)).replace('/*VIEW_CSS*/','\n'.join(css))
    t=t.replace('<!--MAST-->',mast).replace('<!--RADIOS-->','\n'.join(radios)).replace('<!--NAV-->',nav).replace('<!--VIEWS-->','\n'.join(body)).replace('<!--VIEW_JS-->',js)
    t=t.replace('__ELSEWHERE__',json.dumps(elsewhere,separators=(',',':')))
    t=t.replace('__PATHS__',paths).replace('__DATA__',data).replace('__TOPHEX__',A['pal'][0]['hex']).replace('__TOPSHARE__',str(round(A['pal'][0]['share'])))
    kb=round(len(t.encode())/1024); t=t.replace('__KB__',f'{kb:,}')
    left=re.findall(r'__[A-Z]+__|^\s*@@\w+',re.sub(r'data:[^")]+','',re.sub(r'<pre>.*?</pre>','',t,flags=re.S)),flags=re.M); assert not left, left
    open(os.path.join(ROOT,out),'w').write(t); print(f'{key}: {kb} KB, {len(order)} tabs -> {out}')
build('highlights',OUT['highlights'],'','The highlights: photo effects, scroll effects, layouts, post previews for social media, and one message told in six voices. Tap a tab.',HIGHLIGHT_GROUPS,('components.html','Components: pages, decks, more post previews, parts and the skill →'))
build('components',OUT['components'],'Components','Everything else you can build with: pages, decks, post previews for six platforms, parts, design ideas, a picker, the skill and a guide. Tap a tab.',COMPONENT_GROUPS,('studio.html','← Highlights: photo effects, scroll effects, layouts, socials and voices'))
# ---- starters: a deck as one small file with system fonts and no photograph, for an agent to copy and fill
def write_starters():
    lib=open(os.path.join(HERE,'views','01-lib.html')).read()
    eng_css=lib[lib.index('/* deck engine.'):]; eng_css=eng_css[:eng_css.index('</style>')]
    eng_js=lib[lib.index('STUDIO.deck='):]; eng_js=eng_js[:eng_js.index('</script>')]
    eng_css=eng_css.replace('html[data-view^="deck-"] ','')
    out=os.path.join(SKILL,'assets','starters'); os.makedirs(out,exist_ok=True); made=[]
    for f,key,name in (('81-deck-visionary.html','deck-visionary','Visionary deck'),('82-deck-story.html','deck-story','Story deck'),('83-deck-briefing.html','deck-briefing','Briefing deck'),('84-deck-workshop.html','deck-workshop','Workshop deck')):
        v=open(os.path.join(HERE,'views',f)).read()
        css=v[v.index('<style>')+7:v.index('</style>')]
        dk=v[v.index('<div class="dk '):]; dk=dk[:dk.index('</section>\n  <section class="anat">')] if '</section>\n  <section class="anat">' in dk else dk[:dk.index('<section class="anat">')]
        dk=dk.rstrip(); dk=dk[:-len('</section>')].rstrip() if dk.endswith('</section>') else dk
        dk=re.sub(r'<div class="ph ph2"','<div class="ph"',dk)
        css=re.sub(r'var\(--ph-\w+\)','var(--slide-photo,linear-gradient(#1a1a1a,#1a1a1a))',css)   # the starter carries no picture: the picture slides wait for yours
        picnote='     A slide with the class dv-img is a picture with words over it. Give it your photograph by setting --slide-photo on that\n     slide to a url() holding a data: address.\n' if 'dv-img' in dk else ''
        doc=f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name}: starter</title>
<!-- {name}: starter. One file, no outside requests, system fonts, no photograph.
     To use: replace the text in each slide, which is a section with the class dk-s. Keep one idea on each slide.
     The aside with the class dk-note is the speaker's note for that slide. Add or remove slides freely.
     A photograph goes on a slide as the background of a div with the class ph, written into the file as a data: address.
{picnote}     (No tags are written out in this comment, so a search for a tag finds only real ones.)
     Arrow keys, the buttons, a tap or a swipe move between slides. N shows the notes. Print gives one slide a page.
     With scripts off the slides are a readable column.
     Generated by _build/build.py from the same styles and script as the full template. -->
<style>
:root{{--pine:#1b2228;--pine-2:#28343d;--reed:#d2b78c;--fog:#e8edf3;--sans:"Helvetica Neue",Arial,system-ui,sans-serif;--display:"Avenir Next","Segoe UI",system-ui,sans-serif;--text:"Iowan Old Style","Palatino Linotype",Georgia,serif}}
*{{box-sizing:border-box}}html,body{{margin:0}}body{{background:var(--pine);font-family:var(--sans);padding:14px 0}}
h1,h2,h3,p,ol,ul{{margin:0}}button{{font:inherit;cursor:pointer}}
.ph{{background:linear-gradient(135deg,#5b6b4f,#c79a5b 60%,#f1d9a8) center/cover}}
@media print{{body{{padding:0;background:none}}.dk{{padding:0;gap:0;max-width:none}}}}
{eng_css.strip()}
{css.strip()}
</style>
</head>
<body>
{dk}
<script>
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const h=(n,a={{}})=>{{const e=document.createElement(n);for(const k in a)e.setAttribute(k,a[k]);return e}};
const STUDIO={{}};
{eng_js.strip()}
STUDIO.deck(document);
</script>
</body>
</html>
"""
        open(os.path.join(out,key+'.html'),'w').write(doc); made.append((key,len(doc)))
    # social: each artboard as one SVG file with its text styles inside and system fonts
    v=open(os.path.join(HERE,'views','85-social.html')).read()
    css=''.join(l for l in v[v.index('<style>')+7:v.index('</style>')].split('\n') if re.match(r'\.so-[hsn]\{font',l))
    css=css.replace('var(--display)','"Avenir Next","Segoe UI","Helvetica Neue",Arial,sans-serif').replace('"Gloock",serif','Georgia,"Times New Roman",serif')
    for m in re.finditer(r'<svg id="(so-[a-z0-9-]+)" class="so-a"( viewBox="0 0 (\d+) (\d+)".*?</svg>)',v,re.S):
        sid,body,w,hh=m.group(1),m.group(2),m.group(3),m.group(4)
        body=re.sub(r'<image data-photo="2"[^>]*?/>|<image data-photo="2".*?</image>','<!-- a photograph goes here as <image href="data:..."> covering the artboard -->',body,flags=re.S)
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{hh}"'+body.replace('>',f'>\n<!-- Social starter, {w} by {hh}. Change the text and the fill colours. Keep the headline to seven words or fewer. System fonts, so it opens anywhere. Generated by _build/build.py. -->\n<style>{css}</style>',1)
        name='social-'+sid[3:]+'.svg'; open(os.path.join(out,name),'w').write(svg); made.append((name,len(svg)))
    print('starters:',made)
write_starters()


# ---- the index: one machine-readable file and one page for people, both generated, so neither can drift from the templates
def write_design_ideas():
    """The skill's design-ideas card, from the three design views, so the rules exist in one place."""
    V=os.path.join(HERE,'views'); un=lambda x: html.unescape(re.sub(r'<[^>]+>','',x)).strip()
    o=['# Design ideas','','A short, chosen set of ideas for cards, layouts and colour. Use them when you pick the parts and the look.',
       'Generated from the studio\'s design tabs by `_build/build.py`. Edit the views, not this file.','','## Contents','','- Cards','- Layouts','- Colour','- A palette from one brand colour','']
    for g,f,out,head in CONCEPTS:
        t=open(os.path.join(V,f)).read(); o+=[f'## {head}','']
        rules=re.search(r'<ul class="c[do]-rules">(.*?)</ul>',t,re.S)
        if rules: o+=['Rules:','']+[f'- {un(x)}' for x in re.findall(r'<li>(.*?)</li>',rules.group(1),re.S)]+['']
        pick=re.search(r'<table class="ly-pick">.*?<tbody>(.*?)</tbody>',t,re.S)
        if pick: o+=['| The reader has to | Use |','| --- | --- |']+[f'| {un(a)} | {un(b)} |' for a,b in re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td></tr>',pick.group(1),re.S)]+['']
        o+=['| Idea | What it is | Rule or use |','| --- | --- | --- |']
        for sec in re.findall(r'<section class="spec".*?</section>',t,re.S):
            q,effort,made,grow,use=[x.strip() for x in re.search(r'^@@ask (.*)$',sec,re.M).group(1).split('||')]
            rule=re.search(r'<li><b>The rule</b>(.*?)</li>',sec,re.S)
            o.append(f"| {un(re.search(r'<h2>(.*?)</h2>',sec).group(1))} | {un(re.search(r'<p class=\"measure\">(.*?)</p>',sec,re.S).group(1))} | {un(rule.group(1)).capitalize() if rule else 'Use for: '+use.lower()} |")
        o.append('')
    p=C.palette(45)
    o+=['## A palette from one brand colour','','When the person has one brand colour and nothing else, build the rest from its hue. Each role is a fixed lightness and strength in OKLCH, with the hue taken from the brand.','',
        '| Role | Lightness | Chroma | Share of the page |','| --- | --- | --- | --- |']+[f'| {u} | {L} | {Cc} | {str(sh)+" parts" if sh else "as needed"} |' for k,u,L,Cc,sh in C.PALETTE_ROLES]
    o+=['','Write each colour as `oklch(lightness chroma hue)` with a hex value beside it. Then check these pairs and list the ratios in the delivery note:','']+[f"- {k['pair']}: at least {k['needs']:g} to 1" for k in p['checks']]
    o+=['',p['rule'],'','With the studio\'s MCP server connected, `artifact-studio:make_palette` does the sums and the checks.','']
    open(os.path.join(SKILL,'references','design-ideas.md'),'w').write('\n'.join(o))
PHOTO_AT={}
def write_index(parts,photo):
    import datetime
    slug=lambda x: re.sub(r'[^a-z0-9]+','-',x.lower()).strip('-')
    SRC='level-3-files/mcp/library/sources/'; SVG='level-3-files/mcp/library/svg/'; ST='level-2-files/artifact-studio/assets/starters/'; looks=re.findall(r'^## (.+)$',open(SKILL+'/references/looks.md').read(),re.M)
    looks=[l for l in looks if l in ('Clean','Cinematic','Scrollytelling','Dashboard','Editorial','Keynote black','Paper memo','Field guide','Faded film')]
    tpl=[]
    for t in C.TEMPLATES:
        view=TAB[t['id']]; lv=LV.get(t['id'])
        ask={'short':lv[0],'full':lv[1],'with_skill':lv[2]} if lv else {'short':t['ask']}
        e=dict(id=t['id'],kind=t['kind'],title=t['title'],summary=t['summary'],preview=pv(view),source=SRC+VFILE[view],fit=t['fit'],options=C.OPTIONS[t['kind']],ask=ask)
        for k in('look','size','voice'):
            if k in t: e[k]=t[k]
        if t['kind']=='voice': e['default_look']=C.RULES['look_for_voice'][t['id']]
        tpl.append(e)
    comp=[dict(id='page-'+slug(n),group='page',name=n,use=use.rstrip('.'),ask=q,effort=effort,preview=pv('parts'),source=SRC+'30-parts.html') for n,blurb,q,effort,made,grow,use in parts]
    comp+=[dict(id='photo-'+slug(n),group='photo',name=n,use=blurb,ask=q,effort=effort,preview=pv(PHOTO_AT[n][1]),source=SRC+PHOTO_AT[n][0]) for n,blurb,q,effort,made,grow,use in photo]
    for g,f,out,_ in CONCEPTS:
        for sec in re.findall(r'<section class="spec".*?</section>',open(os.path.join(HERE,'views',f)).read(),re.S):
            q,effort,made,grow,use=[x.strip() for x in re.search(r'^@@ask (.*)$',sec,re.M).group(1).split('||')]
            n=re.search(r'<h2>(.*?)</h2>',sec).group(1)
            comp.append(dict(id=g+'-'+slug(n),group=g,name=n,use=html.unescape(re.search(r'<p class="measure">(.*?)</p>',sec,re.S).group(1)),ask=html.unescape(q),effort=effort,preview=pv(g+'s' if g!='colour' else 'colour'),source=SRC+f))
    un=lambda x: html.unescape(re.sub(r'<[^>]+>','',x)).strip()
    for v in POSTS:
        s=open(os.path.join(HERE,'views',VFILE[v])).read()
        comp.append(dict(id=v,group='post',name=LABEL[v]+' post preview' if v not in('post-email','post-blog') else LABEL[v]+' preview',use=un(re.search(r'<p class="sp-lede-top">(.*?)</p>',s,re.S).group(1)),ask=un(re.findall(r'<blockquote>(.*?)</blockquote>',s,re.S)[-1]),effort='One sentence, your notes and your photos',preview=pv(v),source=SRC+VFILE[v]))
    comp+=[dict(id='svg-'+name[:-4],group='svg',name=title,use=desc,ask=f'Add the "{name[:-4]}" animated SVG from the artifact studio, recoloured to my accent colour.',effort='Copy one file',file=SVG+name,source=SVG+name) for name,title,desc,_ in svg_items()]
    for t in tpl:
        st=sorted(glob.glob(os.path.join(ROOT,ST,t['id']+'*')))
        if st: t['starter']=[os.path.relpath(x,ROOT) for x in st] if len(st)>1 else os.path.relpath(st[0],ROOT)
    kinds=['page','voice','deck','social']
    counts={'templates':len(tpl),**{k+'s' if k!='social' else 'social_formats':sum(t['kind']==k for t in tpl) for k in kinds},'components':len(comp),'page_parts':len(parts),'photo_parts':len(photo),'animated_svg':sum(c['group']=='svg' for c in comp),'design_ideas':sum(c['group'] in('card','layout','colour') for c in comp),'post_previews':sum(c['group']=='post' for c in comp),'looks':len(looks)}
    idx=dict(name='artifact-studio',generated=datetime.date.today().isoformat(),
             read_me='Paths are relative to the project folder. "preview" is the file and tab that shows it: base/studio.html holds the highlights and base/components.html holds the rest. "starter", where present, is a small complete file to copy and fill. "source" is reference code: one style block, the markup and one script, not a complete file. A post preview also needs the frame styles in sources/02-posts-lib.html. "fit" scores run 0 to 3. To choose, score = 3 x goal fit + 2 x audience fit, highest first.',
             counts=counts,social_styles=C.SOCIAL_STYLES,facets={f:[dict(id=k,label=v) for k,v in v2] for f,v2 in C.FACETS.items()},rules=C.RULES,templates=tpl,components=comp,
             looks=[dict(name=l,preview=pv('looks'),card='level-2-files/artifact-studio/references/looks.md') for l in looks])
    os.makedirs(os.path.join(LIBRARY,'sources'),exist_ok=True); os.makedirs(os.path.join(LIBRARY,'svg'),exist_ok=True)
    json.dump(idx,open(os.path.join(LIBRARY,'index.json'),'w'),indent=1)
    keep={os.path.basename(x['source']) for x in tpl+comp if x['source'].startswith(SRC)}|{'02-posts-lib.html','86-socials.html'}   # the shared frame styles, and the page that shows three drafts side by side
    for f in os.listdir(os.path.join(LIBRARY,'sources')):   # a view removed from views/ leaves the library too
        if f.endswith('.html') and f!='shell.html' and f not in keep: os.remove(os.path.join(LIBRARY,'sources',f))
    for f in sorted(keep): shutil.copy(os.path.join(HERE,'views',f),os.path.join(LIBRARY,'sources',f))
    for f in sorted(glob.glob(os.path.join(SVGDIR,'*.svg'))): shutil.copy(f,os.path.join(LIBRARY,'svg'))
    shutil.copy(os.path.join(HERE,'shell.html'),os.path.join(LIBRARY,'sources','shell.html'))
    open(os.path.join(ROOT,'level-3-files','mcp','catalog.py'),'w').write('# Generated: a copy of _build/catalog.py, made by _build/build.py so the server needs nothing outside this folder and the skill. Edit that file, not this one.\n'+open(os.path.join(HERE,'catalog.py')).read())
    line=f"{counts['templates']} templates ({counts['pages']} pages, {counts['voices']} voices, {counts['decks']} decks, {counts['social_formats']} social formats), {counts['components']} components ({counts['page_parts']} page parts, {counts['photo_parts']} photo parts, {counts['animated_svg']} animated SVG files, {counts['design_ideas']} design ideas for cards, layouts and colour, {counts['post_previews']} post previews) and {counts['looks']} looks"
    for readme in (os.path.join(ROOT,'README.md'),):
        t=open(readme).read(); t2=re.sub(r'<!-- counts -->.*?<!-- /counts -->',f'<!-- counts -->{line}<!-- /counts -->',t,flags=re.S)
        if t2!=t: open(readme,'w').write(t2)
    for k,n in re.findall(r'data-n="(\w+)" data-count="(\d+)"',VIEW['voice-keynote']): assert counts[k]==int(n), f'41-voice-keynote.html says {n} for {k}; the library has {counts[k]}. Update the view.'
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
    photo=[]; pt=''
    for pf,ptab in (('20-photo.html','photo'),('21-scroll.html','scroll'),('22-lookvoice.html','lookvoice')):
     pt+=read(pf)
     for sec in re.findall(r'<section class="spec".*?</section>',read(pf),re.S):
        name=re.search(r'<h2>(.*?)</h2>',sec).group(1); facts=dict((a,un(b)) for a,b in re.findall(r'<dt>(.*?)</dt><dd>(.*?)</dd>',sec)); PHOTO_AT[name]=(pf,ptab)
        q=re.search(r'<blockquote[^>]*>(.*?)</blockquote>',sec,re.S).group(1).strip()
        photo.append((name,un(re.search(r'<p class="measure">(.*?)</p>',sec,re.S).group(1)),un(q),facts['Effort'],facts['Made here with'],facts['Grow into'],facts['Seen in']))
    looks=re.findall(r"\{id:'(\w+)',name:'([^']+)',line:'([^']+)',voice:'([^']+)',by:'([^']+)',ask:'([^']+)'\}",pt)
    o=['# Sentences','','Every sentence in the studio, in one place. Copy one, attach your notes (and a photo if the page uses one), and paste both into a chat assistant.','',
       '**Status: untested.** These sentences describe what the demo pages do. They have not yet been run in fresh chats and scored.','',
       'This file is generated from the examples by `_build/build.py`. Edit the views, not this file.','']
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
    open(os.path.join(HERE,'sentences.md'),'w').write('\n'.join(o).rstrip()+'\n')
    c=['# Component catalogue','','The parts a page can be built from. Each row is a working example in the studio. Pick parts that carry content; never add one for decoration.','',
       'Generated from the examples by `_build/build.py`.','']
    for head,rows in (('Page components (no photo needed)',parts),('Photo components',photo)):
        c+=[f'## {head}','','| Component | What it is for | How it is made | Grow into |','| --- | --- | --- | --- |']
        c+=[f'| {n} | {b} | {made} | {grow} |' for n,b,q,effort,made,grow,use in rows]+['']
    sk=os.path.join(SKILL,'references','components.md')
    write_design_ideas()
    write_index(parts,photo)
    open(sk,'w').write('\n'.join(c).rstrip()+'\n'); print('docs:',len(lv),'level sets,',len(parts),'page parts,',len(photo),'photo parts')
export_docs()
