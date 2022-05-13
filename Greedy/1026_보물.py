#1026_보물
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sorted_a = sorted(a, reverse=True)
sorted_b = sorted(b)

res=0
for i in range(n):
    res+=sorted_b[i]*sorted_a[i]

print(res)
