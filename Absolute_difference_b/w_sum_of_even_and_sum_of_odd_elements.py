n=int(input())
arr=list(map(int,input().split()))[:n]
so=0
se=0
for i in range(0,n):
    if arr[i]%2==0:
        se=se+arr[i]
    else:
        so=so+arr[i]
print(abs(se-so))
    