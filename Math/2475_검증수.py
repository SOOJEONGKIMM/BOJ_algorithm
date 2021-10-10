import sys
input = sys.stdin.readline
s = [i ** 2 for i in map(int, input().split())]
print(sum(s) % 10)
