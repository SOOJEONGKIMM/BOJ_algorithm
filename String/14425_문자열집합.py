#14425_문자열집합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

S = {input().rstrip() for _ in range(N)}
cnt=0
for _ in range(M):
    search = input().rstrip()
    if search in S:
        cnt += 1

print(cnt)
