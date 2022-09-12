n=int(input())
l=list(map(int,input().split()))[:n]
ln=n-1
while(True):
    if l[ln]%2==0:
        print(l[ln])
        break
    ln-=1