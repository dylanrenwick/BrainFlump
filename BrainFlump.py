import sys,random
a=sys.argv
if len(a)!=3:exit()
if a[1]=='-f':f=open(a[2],'w');o=f.readall();f.close()
elif a[1]=='-c':o=a[2]
v=0
d=[]
for i in range(0,len(o)):
 c=o[i]
 if c=='+':v+=1
 elif c=='-':v-=1
 elif c==':':d.append(v)
 elif c==';':v=d.pop(random.randint(0,len(d)-1))
 elif c=='(':exit()
 elif c==')':exit()
 elif c==',':v=ord(sys.stdin.read(1))
 elif c=='.':sys.stdout.write(chr(v%127))

