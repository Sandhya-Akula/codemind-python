n=int(input())
t=n
s=0
if n<0:
    n=n*-1
while(n>0):
    r=n%10
    n=n//10
    s=s*10+r
if t<0:
    print(s*-1)
else:
    print(s)
    