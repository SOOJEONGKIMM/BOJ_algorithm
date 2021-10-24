#2980_도로와신호등
import sys
N, L = map(int, input().split())
time=0
cur = 0

for _ in range(N):
    D, R, G = map(int, input().split())
    time += D - cur
    cur = D
    red = time % (R + G)
    if(red <= R):
        time += R - red
time+=(L - cur)
print(time)
