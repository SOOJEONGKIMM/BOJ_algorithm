#2548_대표 자연수
import sys
input = sys.stdin.readline

N = int(input())

real = list(map(int,input().split()))

real.sort()

left, right = divmod(N, 2)

print(real[left+right-1])
