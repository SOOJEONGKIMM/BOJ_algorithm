#2908 상수
import sys
input = sys.stdin.readline

a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a>b:        
    print(a)
else:
    print(b)

