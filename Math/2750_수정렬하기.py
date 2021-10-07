import sys
input = sys.stdin.readline

N = int(input())
n = []
for _ in range(N):
    n.append(int(input()))

n.sort()
for i in range(N):
    print(n[i], end='\n')
