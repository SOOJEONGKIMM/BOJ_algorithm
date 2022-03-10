#1655_가운데를 말해요
import heapq
import sys
n=int(sys.stdin.readline())
min_h, max_h = [], []
for _ in range(n):
    num=int(sys.stdin.readline())
    if len(max_h)==len(min_h):
        heapq.heappush(max_h, (-num, num))#(priority, value)
    else:
        heapq.heappush(min_h, (num, num))

    if min_h and max_h[0][1] > min_h[0][1]:
        max_val = heapq.heappop(max_h)[1]
        min_val = heapq.heappop(min_h)[1]
        heapq.heappush(max_h, (-min_val, min_val))
        heapq.heappush(min_h, (max_val, max_val))

    print(max_h[0][1])
