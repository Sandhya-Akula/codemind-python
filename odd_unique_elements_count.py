n=int(input())
arr=list(map(int,input().split()))
a=[]
cnt=0
for i in arr:
    if i not in a:
        a.append(i)
for i in a:
    if i%2!=0:
        cnt+=1
print(cnt)