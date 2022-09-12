n=int(input())
l=list(map(int,input().split()))[:n]
num=int(input())
if num in l:
    print("True")
else:
    print("False")