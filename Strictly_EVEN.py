def strickeven(arr):
    if len(arr)==1:
        return True
    for i in range(len(arr)):
        if arr[i]%2==0:
            if i%2!=0:
                return False
    return True

n=int(input())
arr=list(map(int,input().split()))
print(strickeven(arr))