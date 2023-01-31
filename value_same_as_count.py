n=int(input())
a=list(map(int,input().split()))
d=[]
s=0
for i in a:
    if i not in d:
        d.append(i)
for i in range(len(d)):
    if d[i]==a.count(d[i]):
        s+=1
print(s)