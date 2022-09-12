n=int(input())
l=list(map(int,input().split()))[:n]
c=l[0]
for i in range(0,n):
    if l[i]<=c:
        c=l[i]
print(c)