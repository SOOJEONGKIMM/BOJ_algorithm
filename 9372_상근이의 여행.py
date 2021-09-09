import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    for _ in range(M):
        a, b = map(int, input().split())

        #connected graph: N-1

    print(N-1)
