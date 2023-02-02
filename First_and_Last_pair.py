n=int(input())
arr=list(map(int,input().split()))
j=n-1
if n%2==0:
    for i in range(0,n):
        print(arr[i],arr[j],end=" ")
        j=j-1
        if i>=j:
            break
        
else:
    for i in range(0,n):
        print(arr[i],end=" ")
        if i==j:
            break
        else:
            print(arr[j],end=" ")
        j=j-1
if n%2!=0:
    print(0)