n=int(input())
arr=list(map(int,input().split()))
d={}
l=[]
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key in d:
    if key==d[key]:
        l.append(key)
if len(l)==0:
    print(-1)
elif len(l)==1:
    print(l[0],l[0])
else:
    print(min(l),max(l))