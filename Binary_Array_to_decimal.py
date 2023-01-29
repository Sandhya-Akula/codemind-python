n=int(input())
arr=list(map(int,input().split()))
l=n-1
s=0
for i in arr:
    s+=(2**l)*i
    l=l-1
print(s)
    
    