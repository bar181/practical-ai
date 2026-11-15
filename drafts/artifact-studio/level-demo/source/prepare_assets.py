"""Prepare everything the gallery page embeds: the photo, measurements taken from it,
line art traced from it, and subset fonts. Writes assets.json next to this script.

Usage: python3 prepare_assets.py --photo photo.jpg --fonts path/to/font/folder
The font folder must hold NationalPark-Bold.ttf, NationalPark-Regular.ttf, CrimsonPro-Regular.ttf,
CrimsonPro-Italic.ttf and CrimsonPro-Bold.ttf (both families are on Google Fonts, SIL OFL 1.1).
Needs: pillow, numpy, fonttools, brotli.
"""
import argparse, base64, io, json, random, subprocess, os, tempfile
from PIL import Image, ImageOps
import numpy as np
ap=argparse.ArgumentParser(); ap.add_argument('--photo',default='photo.jpg'); ap.add_argument('--fonts',default='fonts'); ap.add_argument('--quality',type=int,default=72)
args=ap.parse_args()
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=args.photo
im = ImageOps.exif_transpose(Image.open(SRC)).convert('RGB')
W0,H0 = im.size
buf=io.BytesIO(); im.save(buf,'JPEG',quality=args.quality,optimize=True,progressive=True)  # saved without metadata
photo=base64.b64encode(buf.getvalue()).decode()
# analysis on 1600x1200
a=np.asarray(im.resize((1600,1200),Image.LANCZOS)).astype(float); H,W,_=a.shape
lum=(0.2126*a[...,0]+0.7152*a[...,1]+0.0722*a[...,2])/255
N=48
rows=[]; 
for i in range(N):
    y0,y1=int(i*H/N),int((i+1)*H/N)
    c=a[y0:y1].reshape(-1,3).mean(0)
    rows.append({'b':round(float(lum[y0:y1].mean())*100,1),'c':'#%02x%02x%02x'%tuple(int(round(v)) for v in c)})
def first_dark(x,y0,y1,th,w=10):
    col=lum[y0:y1,x:x+w].mean(axis=1); idx=np.where(col<th)[0]
    return int(y0+idx[0]) if len(idx) else None
tree=[(x,first_dark(x,600,790,0.36)) for x in range(0,1150,10)]
isl=[(x,first_dark(x,600,790,0.36)) for x in range(1250,1600,10)]
# bottom of far shore = first bright row below treeline
def shore_bottom(x,y):
    col=lum[y:y+80,x:x+10].mean(axis=1); idx=np.where(col>0.5)[0]
    return int(y+idx[0]) if len(idx) else y+30
trunk=[]
for y in range(0,900,25):
    r=lum[y:y+25,1080:1340].mean(axis=0); d=np.where(r<0.36)[0]
    runs=[];s=p=d[0]
    for v in d[1:]:
        if v!=p+1: runs.append((s,p)); s=v
        p=v
    runs.append((s,p)); s,p=max(runs,key=lambda t:t[1]-t[0]); trunk.append((y+12,1080+int(s),1080+int(p)))
# smooth trunk edges with linear fit
ys=np.array([t[0] for t in trunk]); L=np.polyfit(ys,[t[1] for t in trunk],2); R=np.polyfit(ys,[t[2] for t in trunk],2)
reed=[]
for x in range(0,1600,8):
    if 1120<x<1300: continue
    col=lum[770:1000,x:x+8].mean(axis=1)
    y=None
    for i in range(len(col)-25):
        if col[i]<0.42 and col[i:i+25].mean()<0.45: y=770+i; break
    reed.append((x,y if y else 900))
# kmeans palette
small=np.asarray(im.resize((160,120))).reshape(-1,3).astype(float)
rng=np.random.default_rng(3);k=6;c=small[rng.choice(len(small),k,replace=False)]
for _ in range(60):
    d=((small[:,None]-c[None])**2).sum(-1); l=d.argmin(1)
    c=np.array([small[l==i].mean(0) if (l==i).any() else c[i] for i in range(k)])
cnt=np.bincount(l,minlength=k)/len(l)
pal=[{'hex':'#%02x%02x%02x'%tuple(int(round(v)) for v in c[i]),'share':round(float(cnt[i])*100,1)} for i in np.argsort(-cnt)]
# ---- line art paths (viewBox 1600x1200)
def poly(pts): return 'M'+' L'.join(f'{x},{y}' for x,y in pts)
P={}
P['tree']=poly([(x,y) for x,y in tree if y])
P['shore']=poly([(x,shore_bottom(x,y)) for x,y in tree if y][::-1])
P['isl']=poly([(x,y) for x,y in isl if y])
tl=[(round(float(np.polyval(L,y))),y) for y in range(0,1001,50)]; tr_=[(round(float(np.polyval(R,y))),y) for y in range(0,1001,50)]
P['trunkL']=poly(tl); P['trunkR']=poly(tr_)
random.seed(11)
bark=[]
for i in range(26):
    y=random.randint(20,900); xl=np.polyval(L,y); xr=np.polyval(R,y); x=xl+(xr-xl)*random.uniform(.15,.85); h=random.randint(25,70)
    bark.append(f'M{x:.0f},{y} l{random.randint(-3,5)},{h}')
P['bark']=' '.join(bark)
P['branches']=' '.join([
 'M1150,175 Q1040,150 960,120 Q900,95 862,88','M1040,150 Q1010,110 985,70','M990,128 Q950,150 905,165','M1010,137 Q1000,95 1030,60',
 'M1152,235 Q1090,260 1040,300 Q1010,330 1000,345','M1090,262 Q1075,300 1085,335','M1160,400 Q1110,415 1070,450 Q1060,470 1085,478',
 'M1208,235 Q1262,270 1284,320 Q1296,380 1272,446','M1205,95 Q1270,60 1330,22','M1270,60 Q1300,75 1320,110',
 'M1600,95 Q1500,110 1418,128 Q1450,90 1470,60','M1500,110 Q1520,150 1560,170'])
rip=[]
for i in range(16):
    y=random.randint(722,790); x=random.randint(20,1050); w=random.randint(50,170); rip.append(f'M{x},{y} h{w}')
for i in range(5):
    y=random.randint(730,800); x=random.randint(1300,1500); rip.append(f'M{x},{y} h{random.randint(40,90)}')
P['ripples']=' '.join(rip)
P['bush']='M905,760 Q880,740 872,728 M905,760 Q896,735 890,722 M905,760 Q906,738 910,724 M905,760 Q922,742 934,730 M905,760 Q930,752 942,746 M880,762 h52'
rd=[]
for x,y in reed:
    for j in range(1):
        xx=x+random.randint(0,7); top=y-random.randint(0,38); base=min(1010,y+random.randint(60,170)); lean=random.randint(-14,14)
        rd.append(f'M{xx},{base} Q{xx+lean//2},{(top+base)//2} {xx+lean},{top}')
P['reeds']=' '.join(rd)
cat=[]
for x,y in reed[::7]:
    xx=x+random.randint(-6,6); t=y-random.randint(30,60); cat.append(f'M{xx},{t} v{random.randint(16,24)}')
P['cattails']=' '.join(cat)
P['ground']='M0,1010 Q300,985 620,1040 T1150,1030 T1600,1000'
# ---- fonts
FD=args.fonts.rstrip('/')+'/'; TMP=tempfile.mkdtemp()
fonts={}
for name,f in [('np7','NationalPark-Bold.ttf'),('np4','NationalPark-Regular.ttf'),('cp4','CrimsonPro-Regular.ttf'),('cp4i','CrimsonPro-Italic.ttf'),('cp7','CrimsonPro-Bold.ttf')]:
    out=os.path.join(TMP,name+'.woff2')
    subprocess.run(['pyftsubset',FD+f,'--unicodes=U+0020-007E,U+00A0,U+00B7,U+00D7,U+2013,U+2014,U+2018,U+2019,U+201C,U+201D,U+2026,U+2192','--flavor=woff2','--layout-features=kern,liga','--output-file='+out],check=True)
    fonts[name]=base64.b64encode(open(out,'rb').read()).decode(); print(name,os.path.getsize(out))
json.dump({'photo':photo,'w':W0,'h':H0,'rows':rows,'pal':pal,'paths':P,'fonts':fonts},open(os.path.join(HERE,'assets.json'),'w'))
print('photo kb',len(photo)//1024,'size',W0,H0); 