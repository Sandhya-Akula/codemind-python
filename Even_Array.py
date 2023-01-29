n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    if i%2!=0:
        s=1
        print("False")
        break
if s==0:
    print("True")
    