l=int(input())
arr=list(map(int,input().split()))[:l]
a,b=map(int,input().split())
s=0 
for i in arr:
    if i<a or i>b:
        s=s+i
print(s)