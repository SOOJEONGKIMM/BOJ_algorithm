#7795_먹을것인가 먹힐것인가
import sys
input = sys.stdin.readline

def bin_search(target, data):
    start = 0
    end = len(data)-1
    res = -1
    while start <= end:
        mid = (start+end) // 2
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid -1
    return res

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt=0
    for i in A:
        cnt += bin_search(i, B) + 1

    print(cnt)

    
