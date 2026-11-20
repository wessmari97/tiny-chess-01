import json as j,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
H="abcdefgh"
V=(0,100,320,330,500,900,0)
T=b"::::;<<6;98::::>;;<?<<>@DDDD::::024426::4:<=4;=>68888:::8:;<8;;<::::;<<<9:::9:::68898:::8:;;9:;;4220422042204220"
N=(-33,-31,-18,-14,14,18,31,33);R=(1,16,-1,-16);D=(15,17,-15,-17)
BG=6e4;TT={};nd=[0]
X=Exception
def P(p,b):
 r=u.Request(E+p,j.dumps(b).encode(),{"content-type":"application/json"})
 with u.urlopen(r)as s:return j.load(s)
def G(u):return H.index(u[0])+(int(u[1])-1)*16
def F(f):
 a=f.split();b=bytearray(128);s=112
 for ch in a[0]:
  if ch=="/":s-=24
  elif ch.isdigit():s+=int(ch)
  else:b[s]="pnbrqk".index(ch.lower())+1+ch.islower()*8;s+=1
 return b,a[1]=="w",sum(1<<"KQkq".index(x)for x in a[2]if x in"KQkq")
def A(b,s,w):
 q=0 if w else 8
 for ds,pc in (((-15,-17)if w else(15,17),1),(N,2),(R+D,6)):
  if any(not(s+d)&136 and b[s+d]==pc+q for d in ds):return 1
 for ds,pc in ((R,4),(D,3)):
  for d in ds:
   t=s+d
   while not t&136:
    p=b[t]
    if p:
     if p in(pc+q,5+q):return 1
     break
    t+=d
 return 0
def K(b,w):return next((q for q in range(128)if b[q]==(6 if w else 14)),-1)
def Z():
 nd[0]+=1
 if nd[0]>BG:raise X
def M(b,w,c):
 m=[]
 def ap(u):m.extend(s|u<<7|q<<14 for q in(5,4,3,2))if(u>>4)==7*w else m.append(s|u<<7)
 for s in range(128):
  if s&136:continue
  p=b[s]
  if not p or(p<8)!=w:continue
  t=p&7
  if t==1:
   d=16 if w else-16
   u=s+d
   if not b[u]:
    ap(u)
    if(s>>4)==(1 if w else 6)and not b[s+2*d]:m.append(s|s+2*d<<7)
   for dd in(d-1,d+1):
    u=s+dd
    if u&136:continue
    q=b[u]
    if q and(q<8)!=w:ap(u)
  elif t==2 or t==6:
   m.extend(s|u<<7 for d in(N,R+D)[t==6]for u in(s+d,)if not u&136 and(not b[u]or(b[u]<8)!=w))
   if t==6:
    for bt,d in((1,1),(2,-1),(4,1),(8,-1)):
     ks=4 if bt<4 else 116
     if c&bt and not any(b[ks+i*d]for i in(1,2,3)if i<3 or d<0)and not any(A(b,ks+i*d,not w)for i in(0,1,2)):m.append(ks|ks+2*d<<7)
  else:
   for d in(D,R,R+D)[t-3]:
    u=s+d
    while not u&136 and not b[u]:m.append(s|u<<7);u+=d
    if not u&136 and b[u]and(b[u]<8)!=w:m.append(s|u<<7)
 return m
def Do(b,f,t,pr,w,c):
 n=bytearray(b);p=n[f];n[f]=0
 if(p&7)==6 and abs(t-f)==2:
  r=t+1 if t>f else t-2;n[t-1 if t>f else t+1]=n[r];n[r]=0
 n[t]=(pr or p&7)+(0 if w else 8)
 for s in(f,t):c&=~{4:3,7:1,0:2,116:12,119:4,112:8}.get(s,0)
 return n,c
def Ev(b):
 s=0;h=0
 for q in range(128):
  if q&136:continue
  p=b[q]
  if p:
   t=p&7;h|=1<<t;r=q>>4 if p<8 else 7-(q>>4);i=(r if t==1 else min(r,7-r))*4+(0 if t==1 else 16*t)+min(q&7,7-(q&7));v=V[t]+(T[i]-48)*5-50;s+=v if p<8 else-v
 return s if h&50 else 0
def Q(b,w,c,a,be):
 Z()
 s=Ev(b)if w else-Ev(b)
 if s>=be:return be
 if s>a:a=s
 for mv in M(b,w,c):
  if not b[mv>>7&127]and not mv>>14:continue
  nb,nc=Do(b,mv&127,mv>>7&127,mv>>14&7,w,c)
  if A(nb,K(nb,w),not w):continue
  sc=-Q(nb,not w,nc,-be,-a)
  if sc>=be:return be
  if sc>a:a=sc
 return a
def S(b,w,c,d,a,be,pl):
 Z()
 if d<=0:return Q(b,w,c,a,be)
 k=bytes(b);y=TT.get(k)
 ms=M(b,w,c)
 if y and y in ms:ms.remove(y);ms.insert(0,y)
 ms.sort(key=lambda m:(-V[b[m>>7&127]&7],V[b[m&127]&7]))
 best=-1e9;bm=0;lg=0
 for mv in ms:
  nb,nc=Do(b,mv&127,mv>>7&127,mv>>14&7,w,c)
  if A(nb,K(nb,w),not w):continue
  lg=1
  sc=-S(nb,not w,nc,d-1,-be,-a,pl+1)
  if sc>best:best=sc;bm=mv
  if sc>a:a=sc
  if a>=be:break
 if not lg:return-1e5+pl if A(b,K(b,w),not w)else 0
 if len(TT)>2e5:TT.clear()
 TT[k]=bm
 return best
def Y(b,w,c,legal):
 mv=[G(u)|G(u[2:])<<7|((("nbrq".index(u[4])+2)if len(u)==5 else 0)<<14)for u in legal]
 sc={};best=mv[0];d=1;nd[0]=0
 while d<64:
  try:
   a=-1e9;bb=best
   for m in sorted(mv,key=lambda x:-sc.get(x,0)):
    nb,nc=Do(b,m&127,m>>7&127,m>>14&7,w,c)
    s=-S(nb,not w,nc,d-1,-1e9,-a,1)
    sc[m]=s
    if s>a:a=s;bb=m
   best=bb;d+=1
  except X:break
 return best
def U(m):
 f=m&127;t=m>>7&127;pr=m>>14&7
 return H[f&7]+str(f//16+1)+H[t&7]+str(t//16+1)+("nbrq"[pr-2]if pr else"")
while 1:
 g=P("/game",{})
 while g["status"]=="your_move":
  b,w,c=F(g["fen"]);g=P("/move",{"game":g["game"],"move":U(Y(b,w,c,g["legal_moves"]))})
 if g["status"]=="done":break
