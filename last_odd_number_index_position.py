n=int(input())
l=list(map(int,input().split()))[:n]
while((n-1)!=0):
    if l[n-1]%2!=0:
        print(n-1)
        break
    n-=1