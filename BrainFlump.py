from sys import*
from random import*
a=argv
v=e=i=0
d=[]
if len(a)!=3:exit()
if'-f'==a[1]:f=open(a[2]);o=f.read();f.close()
if'-c'==a[1]:o=a[2]
def L(s,c,N,r):
 if s.count(c)<N:return-1
 s=s[::r];f=0
 for i in range(len(s)):
	C=s[i]
	if c==C:f+=1
	if f==N:return len(s)-i+len(s)*(r>0)
 return-1
while i<len(o):
 c=o[i]
 if'('==c:e+=1;exec'i=L(o,")",e,1)'*(not d[randrange(len(d))])
 if')'==c:
	if d[randrange(len(d))]:i=L(o,"(",e,-1)-1
	else:e-=1
 exec['v+=1','v-=1','d.append(v)','v=d.pop(randrange(len(d)))','v=ord(stdin.read(1))','stdout.write(chr(v))','0']['+-:;,.'.find(c)]
 i+=1
