#10989_수 정렬하기 3
import sys

n=int(sys.stdin.readline())
program=[0]*10001
for _ in range(n):
    program[int(sys.stdin.readline())]+=1

for i in range(10001):
    if program[i]!=0:
        for j in range(program[i]):
            print(i)
