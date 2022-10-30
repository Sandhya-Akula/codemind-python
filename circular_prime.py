import math
def isprime(n):#5
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
    return True
n=int(input())
if(isprime(n)):
    s=str(n)
    t=int(s[::-1])
    if isprime(t):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        