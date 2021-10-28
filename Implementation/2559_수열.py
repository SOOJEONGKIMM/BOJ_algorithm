#2559_수열
N, K = map(int, input().split())

num =  list(map(int, input().split()))

total = sum(num[:K])
res=[total]
for i in range(N-K):
    group = total - num[i] + num[i+K]
    total = group
    res.append(group)

print(max(res))
