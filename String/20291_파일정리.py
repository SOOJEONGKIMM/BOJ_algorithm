#20291_파일정리
import sys
from collections import Counter
n=int(input())
file_exe=[]
for _ in range(n):
    file = sys.stdin.readline().rstrip()
    file=file.split('.')
    file_exe.append(file[-1])

counter=Counter(file_exe)
counter = dict(sorted(counter.items()))

for i in counter:
    print(i, counter[i])
