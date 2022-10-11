n=int(input())
l=list(map(int,input().split()))[:n]
ans=0
for i in range(0,len(l)-2):
    if l[i]%2==0 and l[i+2]%2!=0:
        ans+=1
    elif l[i]%2!=0 and l[i+2]%2==0:
        ans+=1
    
print(ans)