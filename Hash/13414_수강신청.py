#13414_수강신청
import sys
k,l = map(int,sys.stdin.readline().split())
num=dict()
for i in range(l):
    num[sys.stdin.readline()]=i    



cnt=0
for i in sorted(num.items(), key=lambda x: x[1]):
    if cnt>=k:
        break
    cnt+=1
    print(i[0], end='')
