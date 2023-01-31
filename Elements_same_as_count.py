n=int(input())
arr=list(map(int,input().split()))
d=[]
s=0
for i in arr:
    if i not in d:
        d.append(i)
for i in range(len(d)):
    if d[i]==arr.count(d[i]):
        s=1
        print(d[i],end=" ")
if s==0:
    print(-1)
