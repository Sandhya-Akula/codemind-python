n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
av=s//n
c=0
for i in arr:
    if i>=av:
        c+=1
print(c)