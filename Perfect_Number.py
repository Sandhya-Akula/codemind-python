def perfect_number(number):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
    if sum==number:
        return True
    else:
        return False
number=int(input())
print(perfect_number(number))