#12865_평범한 배낭
n, k = map(int, input().split())
bag=[[0,0]]
for _ in range(n):
    bag.append(list(map(int, input().split())))

knapsack=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        w = bag[i][0]
        v = bag[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])
 
print(knapsack[n][k])
