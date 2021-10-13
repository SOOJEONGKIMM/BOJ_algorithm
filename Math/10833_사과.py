#10833_사과
import sys
input = sys.stdin.readline

N = int(input())
remain=0
for i in range(N):
    student, apple = map(int, input().split())
    remain += apple % student

print(remain)
