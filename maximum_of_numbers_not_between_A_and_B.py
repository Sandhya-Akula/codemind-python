n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
na=[]
s=0
for i in arr:
    if i<a or i>b:
        s=1
        na.append(i)
if s==0:
    print(-1)
else:
    print(max(na))