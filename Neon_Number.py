n=int(input())
sum=0
r=n*n
while(r>0):
    d=r%10
    sum=sum+d
    r=r//10
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")
