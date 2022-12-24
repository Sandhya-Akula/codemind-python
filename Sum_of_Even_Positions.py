n=int(input())
arr=list(map(int,input().split()))[:n]
sum=0
for i in range(0,n):
    if i%2==0:
        sum=sum+arr[i]
print(sum)