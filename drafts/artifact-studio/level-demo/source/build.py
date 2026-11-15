"""Build component-gallery.html from page-template.html and assets.json.

Usage: python3 prepare_assets.py ... then python3 build.py
"""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
import json, re
A=json.load(open(os.path.join(HERE,'assets.json'))); t=open(os.path.join(HERE,'page-template.html')).read()
ff=[('National Park',700,'normal','np7'),('National Park',400,'normal','np4'),('Crimson Pro',400,'normal','cp4'),('Crimson Pro',400,'italic','cp4i'),('Crimson Pro',700,'normal','cp7')]
fonts='\n'.join(f'@font-face{{font-family:"{n}";font-weight:{w};font-style:{s};font-display:swap;src:url(data:font/woff2;base64,{A["fonts"][k]}) format("woff2")}}' for n,w,s,k in ff)
P=A['paths']
order=[('tree',0,.26,''),('shore',.06,.24,'thin'),('isl',.2,.16,''),('trunkL',.3,.2,''),('trunkR',.34,.2,''),('bark',.42,.16,'thin'),('branches',.44,.2,''),('bush',.5,.08,''),('ripples',.5,.16,'thin'),('reeds',.56,.22,'thin'),('cattails',.66,.12,''),('ground',.7,.08,'')]
paths=''.join(f'<path pathLength="1" class="{c}" style="--s:{s};--d:{d}" d="{P[k]}"/>' for k,s,d,c in order)
data=json.dumps({'rows':A['rows'],'pal':A['pal']},separators=(',',':'))
t=t.replace('/*FONTS*/',fonts).replace('/*PHOTO*/',f'--photo:url("data:image/jpeg;base64,{A["photo"]}");').replace('__PATHS__',paths).replace('__DATA__',data)
t=t.replace('__TOPHEX__',A['pal'][0]['hex']).replace('__TOPSHARE__',str(round(A['pal'][0]['share'])))
kb=round(len(t.encode())/1024); t=t.replace('__KB__',f'{kb:,}')
assert '__' not in re.sub(r'data:[^")]+','',t), 'placeholder left'
open(os.path.join(HERE,'..','component-gallery.html'),'w').write(t); print('built',round(len(t.encode())/1024),'KB')
