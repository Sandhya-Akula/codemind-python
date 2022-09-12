n=int(input())
l=list(map(int,input().split()))[:n]
num=int(input())
c=0
for i in range(len(l)):
    if l[i]==num:
        c+=1
print(c)