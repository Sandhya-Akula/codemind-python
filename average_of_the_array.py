n=int(input())
l=list(map(int,input().split()))[:n]
avg=sum(l)/n
print("{:.2f}".format(avg))