import math
def isprime(s):#5
    n=int(math.sqrt(s))
    for i in range(2,n+1):
        if s%i==0:
            return False
    return True
n1=int(input())#1
n2=int(input())#3
s=n1+n2+1#5
while(True):
    if(isprime(s)):
        print(s-(n1+n2))
        break
    else:
        s+=1