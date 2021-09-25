import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rec=[]
for _ in range(N):
    rec.append(list(input()))

search = min(M,N)
pointer = 0
for i in range(N):
    for j in range(M):
        for k in range(search):
            if (i+k)<N and (j+k)<M:
                if rec[i][j]==rec[i][j+k] and rec[i][j]==rec[i+k][j] and rec[i][j]==rec[i+k][j+k]:
                    if pointer < k:
                        pointer = k

print((pointer+1)*(pointer+1))
