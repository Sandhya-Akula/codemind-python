import math
def isprime(i):#5
    n=int(math.sqrt(i))
    for j in range(2,n+1):
        if i%j==0:
            return False
    return True
n1=int(input())
n2=int(input())
for i in range(n1+1,n2):
    if(isprime(i)):
        print(i)