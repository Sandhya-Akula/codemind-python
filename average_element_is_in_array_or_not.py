n=int(input())
l=list(map(int,input().split()))[:n]
avg=sum(l)//n
if avg in l:
    print("True")
else:print("False")