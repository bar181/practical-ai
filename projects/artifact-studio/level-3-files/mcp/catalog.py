# Generated: a copy of _build/catalog.py, made by _build/build.py so the server needs nothing outside this folder and the skill. Edit that file, not this one.
"""The studio's catalogue: every template, what it is for, and the rules that pick between them.

One source for three readers: build.py (which writes templates/index.json and templates/README.md),
the Pick tab of the studio page, and the MCP server in level-3-files/mcp. No dependencies.
"""
FACETS={
 'goal':[('report','Say how something went'),('decide','Get a decision'),('sell','Win a customer'),('teach','Explain how something works'),('inspire','Make people feel a change'),('announce','Tell people something new')],
 'audience':[('customer','A customer'),('executive','A busy decision-maker'),('team','My own team'),('public','People who do not know us'),('learner','Someone learning')],
 'format':[('page','A web page'),('deck','A slide deck'),('social','A social post'),('any','Show me one of each')],
}
RULES={'weights':{'goal':3,'audience':2},
 'look_for_voice':{'voice-keynote':'Keynote black','voice-story':'Cinematic','voice-teacher':'Clean','voice-practical':'Field guide','voice-analyst':'Dashboard','voice-brief':'Paper memo'}}
def _t(id,kind,title,name,file,summary,goal,audience,**kw): return dict(id=id,kind=kind,title=title,name=name,file=file,summary=summary,fit={'goal':goal,'audience':audience},**kw)
TEMPLATES=[
 _t('recipe-report','page','One-page report','one-page report','pages/report.html','How a week, month or project went: the answer, the numbers, what changed, what is next.',{'report':3,'decide':2,'announce':1},{'executive':3,'team':3,'customer':1},article='a one-page report'),
 _t('recipe-proposal','page','Proposal','proposal','pages/proposal.html','Something a customer has to say yes to: the job as understood, three options, a schedule, one accept button.',{'sell':3,'decide':3},{'customer':3,'executive':2},article='a proposal page'),
 _t('recipe-explainer','page','Scrolling explainer','scrolling explainer','pages/explainer.html','How something works, told as a picture that changes while short steps scroll past.',{'teach':3,'announce':2,'inspire':1},{'learner':3,'public':2,'team':2,'customer':2},article='a scrolling explainer'),
 _t('recipe-landing','page','Landing page','landing page','pages/landing.html','One offer and one action for people arriving cold: promise, proof, plan, price, questions.',{'sell':3,'announce':3,'inspire':1},{'public':3,'customer':3},article='a landing page'),
 _t('voice-keynote','voice','Keynote voice','keynote','voices/keynote.html','One idea per screen, huge type, almost no words, and "one more thing".',{'inspire':3,'announce':3,'sell':1},{'public':3,'team':2,'customer':2,'executive':1}),
 _t('voice-story','voice','Storyteller voice','storyteller','voices/storyteller.html','The customer is the hero and you are the guide: hook, problem, plan, stakes, ending.',{'sell':3,'inspire':2,'announce':1},{'customer':3,'public':3}),
 _t('voice-teacher','voice','Teacher voice','teacher','voices/teacher.html','An everyday analogy first, then one worked example, the detail, and questions to check yourself.',{'teach':3},{'learner':3,'team':2,'public':1}),
 _t('voice-practical','voice','Practical instructor voice','practical instructor','voices/practical.html','The idea in one sentence, one analogy, numbered steps with a time on each, one next step.',{'teach':3,'report':1,'decide':1},{'team':3,'learner':2,'customer':2}),
 _t('voice-analyst','voice','Analyst voice','analyst','voices/analyst.html','The answer first, then findings whose headings are full sentences, each with one chart and a "so what".',{'report':3,'decide':2},{'executive':3,'team':2}),
 _t('voice-brief','voice','Executive brief voice','executive brief','voices/brief.html','The decision first, numbered background, one options table including "do nothing", risks, next steps.',{'decide':3,'report':2},{'executive':3}),
 _t('deck-visionary','deck','Visionary deck','visionary deck','decks/visionary.html','Eight black slides in the keynote manner: a villain, one rule, three things, one number, one more thing.',{'inspire':3,'announce':3,'sell':1},{'public':3,'team':3,'executive':1,'customer':1},
    ask='Turn my notes into a keynote-style deck: black slides, one idea each, huge type.',look='Keynote black',voice='voice-keynote'),
 _t('deck-story','deck','Story deck','story deck','decks/story.html','Seven warm slides that follow a story: a person, a problem, a guide, a plan, an ask, the stakes, the ending.',{'sell':3,'inspire':2},{'customer':3,'public':2},
    ask='Turn my notes into a short story deck where my customer is the hero and we are the guide.',look='Editorial',voice='voice-story'),
 _t('deck-briefing','deck','Briefing deck','briefing deck','decks/briefing.html','Six light slides for a decision: the answer first, three reasons, two numbers, the options, what is not known, the decision and a date.',{'decide':3,'report':3,'sell':1},{'executive':3,'team':3,'customer':2},
    ask='Turn my notes into a short briefing deck for a decision: the answer first.',look='Clean',voice='voice-brief'),
 _t('deck-workshop','deck','Workshop deck','workshop deck','decks/workshop.html','Seven slides that teach one skill: a promise, a picture, three steps, a worked example, an exercise, a check and a card to keep.',{'teach':3,'report':1},{'learner':3,'team':3,'public':1},
    ask='Turn my notes into a short workshop deck that teaches one skill, with an exercise.',look='Warm',voice='voice-teacher'),
 _t('social-square','social','Square post','square post','social/formats.html#so-square','1080 by 1080. One claim or quote in seven words or fewer.',{'announce':3,'inspire':3,'sell':1},{'public':3,'customer':2},ask='Make a square social post from this one sentence, in my colours.',size='1080x1080'),
 _t('social-portrait','social','Portrait stat post','portrait stat post','social/formats.html#so-portrait','1080 by 1350. One number, what it means, and a before-and-after bar.',{'report':3,'announce':2,'sell':2},{'public':3,'customer':2,'executive':1},ask='Make a portrait social post with my best number, what it means, and a before-and-after bar.',size='1080x1350'),
 _t('social-story','social','Story','story','social/formats.html#so-story','1080 by 1920. A photograph above, two short lines below.',{'inspire':3,'sell':2,'announce':2},{'public':3,'customer':3},ask='Make an upright story picture from my photo with two short lines under it.',size='1080x1920'),
 _t('social-carousel','social','Three-slide carousel','three-slide carousel','social/formats.html#so-carousel-1','Three pictures of 1080 by 1350: the hook, the steps, the ask.',{'teach':3,'sell':2,'announce':1},{'public':3,'learner':3,'customer':2},ask='Make a three-slide carousel from my notes: a hook that stands alone, the steps, then one ask.',size='3 x 1080x1350'),
 _t('social-link','social','Link preview','link preview','social/formats.html#so-link','1200 by 630. The picture shown when a page is shared as a link.',{'announce':3,'sell':1,'report':1},{'public':3,'customer':2,'executive':1},ask='Make the link preview picture for my page: the title large, my company name small.',size='1200x630'),
]
OPTIONS={ # what can be swapped on each kind of template
 'page':'Voice: any of the seven. Look: any of the nine, your brand, or colours from a photo. Parts: any page part, photo part or animated SVG.',
 'voice':'Recipe: any of the four pages, or a deck. Look: the default named with it, or any of the nine. Parts: any that suit the voice.',
 'deck':'Slides: add or remove, one idea each. Look: any of the nine or your brand. Parts: an animated SVG or one photograph per slide.',
 'social':'Colours and type: your brand. Words: one idea, seven words or fewer in the headline. Picture: your own photograph where the format has one.',
}
_LBL={f:dict(v) for f,v in FACETS.items()}
_FIT={3:'a strong fit',2:'a good fit',1:'a possible fit',0:'not made'}
# Social styles: the same seven pictures in three palettes. Each maps the Studio colours to its own.
# Every text and background pair in each palette has a contrast of at least 5 to 1 (checked when chosen).
SOCIAL_STYLES=[
 dict(id='studio',name='Studio',summary='Slate, fog and a warm brown. The default.',swap={}),
 dict(id='bold',name='Bold',summary='Navy, white, a strong red and yellow. For announcements.',swap={'#1b2228':'#0a2540','#e8edf3':'#ffffff','#774528':'#b3261e','#d2b78c':'#ffd23f','#a5b9d8':'#b9d4f1','#4b596e':'#3a4a5e','#f0d9b0':'#ffe9a8'}),
 dict(id='soft',name='Soft',summary='Plum, cream and terracotta. For stories and thanks.',swap={'#1b2228':'#3b2a3f','#e8edf3':'#fbf3e8','#774528':'#9a4a2f','#d2b78c':'#f2c9a0','#a5b9d8':'#dcc9e0','#4b596e':'#5d4a5f','#f0d9b0':'#fde3c4'}),
]
# ---- colour: one hue in, a checked palette out. The page (views/33-colour.html) carries the same sums in script.
import math
# Each role is a lightness and a chroma in OKLCH, where equal steps of lightness look equal to the eye.
# The hue comes from the brand. Neutrals keep a trace of it so greys do not look dead beside the accent.
PALETTE_ROLES=[('surface','Page background',.97,.012,60),('surface2','Panels and cards',.93,.020,0),('line','Borders and rules',.86,.025,0),
               ('muted','Secondary text',.48,.030,30),('ink','Main text',.22,.030,0),('accent','Buttons and links',.46,.140,10),('accentsoft','Highlights behind text',.92,.050,0)]
def oklch_hex(L,C,H):
    """OKLCH to an sRGB hex colour. Chroma is reduced until the colour fits the screen's range."""
    while True:
        a=C*math.cos(math.radians(H)); b=C*math.sin(math.radians(H))
        l=(L+.3963377774*a+.2158037573*b)**3; m=(L-.1055613458*a-.0638541728*b)**3; s=(L-.0894841775*a-1.2914855480*b)**3
        rgb=[4.0767416621*l-3.3077115913*m+.2309699292*s,-1.2684380046*l+2.6097574011*m-.3413193965*s,-.0041960863*l-.7034186147*m+1.7076147010*s]
        if all(-.0005<=x<=1.0005 for x in rgb) or C<.001: break
        C*=.95
    f=lambda x:12.92*x if x<=.0031308 else 1.055*x**(1/2.4)-.055
    return '#'+''.join(f'{max(0,min(255,round(f(max(0,min(1,x)))*255))):02x}' for x in rgb)
def contrast(h1,h2):
    """WCAG contrast ratio between two hex colours, from 1 to 21."""
    def lum(h):
        v=[int(h[i:i+2],16)/255 for i in (1,3,5)]; v=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in v]
        return .2126*v[0]+.7152*v[1]+.0722*v[2]
    a,b=sorted((lum(h1),lum(h2)),reverse=True); return round((a+.05)/(b+.05),2)
def palette(hue):
    """A palette for one brand hue (0 to 359): seven roles with hex values, their share of the page, and contrast checks."""
    hue=int(hue)%360; col={k:oklch_hex(L,C,hue) for k,_,L,C,_ in PALETTE_ROLES}
    checks=[('Main text on the page background',contrast(col['ink'],col['surface']),7),('Secondary text on the page background',contrast(col['muted'],col['surface']),4.5),
            ('Secondary text on panels',contrast(col['muted'],col['surface2']),4.5),('White text on a button',contrast('#ffffff',col['accent']),4.5),('Links on the page background',contrast(col['accent'],col['surface']),4.5),
            ('Main text on a highlight',contrast(col['ink'],col['accentsoft']),7)]
    return dict(hue=hue,roles=[dict(id=k,use=u,hex=col[k],oklch=f'oklch({L} {C} {hue})',share=sh) for k,u,L,C,sh in PALETTE_ROLES],
                checks=[dict(pair=p,ratio=r,needs=n,passes=r>=n) for p,r,n in checks],
                rule='About 60 parts background, 30 parts text and structure, 10 parts accent, judged by eye and not by counting pixels. The accent is for things to act on and nothing else.')
def score(t,goal,audience): w=RULES['weights']; return w['goal']*t['fit']['goal'].get(goal,0)+w['audience']*t['fit']['audience'].get(audience,0)
def rank(kind,goal,audience): return sorted([t for t in TEMPLATES if t['kind']==kind],key=lambda t:-score(t,goal,audience))
def why(t,goal,audience):
    g=_FIT[t['fit']['goal'].get(goal,0)]; a=_FIT[t['fit']['audience'].get(audience,0)]
    return f"{t['title']}: {g} for \"{_LBL['goal'][goal].lower()}\", {a} for \"{_LBL['audience'][audience].lower()}\"."
def _raw(goal,audience,format):
    """The top combination of one format, before strength is added."""
    out=[]; one=True; limit=1
    if format in('page','any'):
        R=rank('page',goal,audience); V=rank('voice',goal,audience)
        for r,v in [(R[0],V[0]),(R[0],V[1]),(R[1],V[0])][:1 if one else limit]:
            out.append(dict(format='page',templates=[r['id'],v['id']],title=f"{r['title']} in the {v['name']} voice",look=RULES['look_for_voice'][v['id']],score=score(r,goal,audience)+score(v,goal,audience),
                            why=why(r,goal,audience)+' '+why(v,goal,audience),ask=f"Make {r['article']} from my notes in the {v['name']} voice."))
    for kind in('deck','social'):
        if format in(kind,'any'):
            for t in rank(kind,goal,audience)[:1 if one else limit]:
                out.append(dict(format=kind,templates=[t['id']],title=t['title'],look=t.get('look','Your brand colours'),score=score(t,goal,audience),why=why(t,goal,audience),ask=t['ask']))
    return out
def recommend(goal,audience,format='any',limit=3):
    """Return up to `limit` combinations for one format, or the best one of each format for 'any'."""
    if goal not in _LBL['goal'] or audience not in _LBL['audience'] or format not in _LBL['format']: raise ValueError('unknown goal, audience or format')
    out=[]; one=format=='any'
    if format in('page','any'):
        R=rank('page',goal,audience); V=rank('voice',goal,audience)
        for r,v in [(R[0],V[0]),(R[0],V[1]),(R[1],V[0])][:1 if one else limit]:
            out.append(dict(format='page',templates=[r['id'],v['id']],title=f"{r['title']} in the {v['name']} voice",look=RULES['look_for_voice'][v['id']],score=score(r,goal,audience)+score(v,goal,audience),
                            why=why(r,goal,audience)+' '+why(v,goal,audience),ask=f"Make {r['article']} from my notes in the {v['name']} voice."))
    for kind in('deck','social'):
        if format in(kind,'any'):
            for t in rank(kind,goal,audience)[:1 if one else limit]:
                out.append(dict(format=kind,templates=[t['id']],title=t['title'],look=t.get('look','Your brand colours'),score=score(t,goal,audience),why=why(t,goal,audience),ask=t['ask']))
    for k,r in enumerate(out):
        r['strength'],r['note']=_strength(r,goal,audience,format)
        if k: r['note']=''          # only the top answer names a better shape
    return out
def _ratio(r): return r['score']/(15*len(r['templates']))
def _strength(r,goal,audience,format):
    """strong from 0.8 of the highest possible score, fair from 0.6, weak below. A weak answer names a better shape."""
    q=_ratio(r); s='strong' if q>=.8 else 'fair' if q>=.6 else 'weak'
    if s!='weak' or format=='any': return s,''
    best=max((x for k in('page','deck','social') if k!=format for x in _raw(goal,audience,k)),key=_ratio)
    return s,(f'{best["title"]} suits this better.' if _ratio(best)>q else '')
