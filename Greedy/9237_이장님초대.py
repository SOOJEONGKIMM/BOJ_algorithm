#9237_이장님초대
n=int(input())

t=list(map(int,input().split()))

t.sort(reverse=True)
for i in range(len(t)):
    t[i]+= i + 1
print(t)
print(max(t)+1)
