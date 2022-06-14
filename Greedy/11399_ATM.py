#11399_ATM.py
n=int(input())
p=list(map(int,input().split()))

p.sort()
res=0
res_box=[]
for i in p:
    res+=i
    res_box.append(res)

print(sum(res_box))
