#2910_빈도 정렬
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

message = list(map(int, input().split()))



cnt = {}

for i in message:
    if i not in cnt:
        cnt[i]=0

    cnt[i] += 1

cnt=sorted(cnt.items(), key=lambda x: x[1], reverse=True)


for key, value in cnt:
    for i in range(value):
        print(str(key), end=" ")
