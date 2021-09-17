import sys
input = sys.stdin.readline

n = int(input())
tri = []

for _ in range(0, n):
    tri.append(list(map(int, input().split())))

row = 2
for i in range(1, n):
    for j in range(row):
        if j==0: #맨 왼쪽 번호
            tri[i][j] +=  tri[i-1][j]
        elif j==len(tri[i])-1: #맨 오른쪽 번호 
            tri[i][j] +=  tri[i-1][j-1]
        else:#그 사이
            tri[i][j] += max(tri[i-1][j],tri[i-1][j-1])
    row += 1

print(max(tri[n-1]))
