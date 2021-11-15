#1037_약수
import sys
num = sys.stdin.readline()
divisor = list(map(int, input().split()))
d_max = max(divisor)
d_min = min(divisor)

print(d_min * d_max)
