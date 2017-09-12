from sys import*
from random import*
a=argv
v=e=i=0
d=[]
if len(a)!=3:exit()
if'-f'==a[1]:f=open(a[2]);o=f.read();f.close()
if'-c'==a[1]:o=a[2]
def L(s,c,N):
 if s.count(c)<N:return-1
 s=s[::-1];f=0
 for i in range(len(s)):
	C=s[i]
	if c==C:f+=1
	if f==N:return len(s)-i
 return-1
def F(s,c,N):
 if s.count(c)<N:return-1
 f=0
 for i in range(len(s)):
	C=s[i]
	if C==c:f+=1
	if f==N:return i
 return-1
while i<len(o):
 c=o[i]
 if'('==c:e+=1;exec'i=L(o,")",e)'*(not v)
 if')'==c:
	if v:i=F(o,"(",e)
	else:e-=1
 exec['v+=1','v-=1','d.append(v)','v=d.pop(randrange(len(d)))','v=ord(stdin.read(1))','stdout.write(chr(v))','0']['+-:;,.'.find(c)]
 i+=1
