#1764_듣보잡
n,m=map(int,input().rstrip().split())

hear=set()
watch=set()
for _ in range(n):
    hear.add(input())
for _ in range(m):
    watch.add(input())



res = sorted(list(hear & watch))



print(len(res))
for i in range(len(res)):
    print(res[i])
