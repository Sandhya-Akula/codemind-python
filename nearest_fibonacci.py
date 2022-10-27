n=int(input())
a=1
b=1
while(True):#2 3 5 8 13
    c=a+b
    a=b
    b=c
    if c>n:
        if abs(b-n)>abs(a-n):
            print(a)
            break
        elif abs(b-n)==abs(a-n):
            print(a,b,end=" ")
            break
        else:
            print(b)
            break
