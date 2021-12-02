#12605_단어순서 뒤집기
import sys
n = int(input())

for i in range(n):
    arr=list(map(str,sys.stdin.readline().strip().split()))
    arr.reverse()
    ans = " ".join(arr)
    print(f"Case #{i+1}: {ans}")
