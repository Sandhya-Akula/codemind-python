n=int(input())
arr=list(map(int,input().split()))
ele_cnt={}
l=[]
for i in arr:
    if i in ele_cnt:
        ele_cnt[i]+=1
    else:
        ele_cnt[i]=1
for key in ele_cnt:
    if key == ele_cnt[key]:
        l.append(key)
if len(l)==0:
    print(-1)
else:
    avr=sum(l)/len(l)
    print("{:.2f}".format(avr))
