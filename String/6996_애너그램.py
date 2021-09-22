#6996: 애너그램
import sys
input = sys.stdin.readline

T = int(input())
ana = []
for i in range(T):
    a, b = map(str,input().split())
    x = sorted(a)
    y = sorted(b)

    if x == y:
        print(a, "&", b, "are anagrams.")
    else:
        print(a, "&", b, "are NOT anagrams.")
