import sys
input = sys.stdin.readline

n = int(input())
seq = []
seq = map(int, input().split())
x = int(input())

seq = sorted(seq)

start = 0
end = n-1
cnt = 0
while start < end:
    if seq[start]+seq[end] == x:
        cnt += 1
    elif seq[start]+seq[end] < x:
        start+=1
        continue
    end-=1


print(cnt)
