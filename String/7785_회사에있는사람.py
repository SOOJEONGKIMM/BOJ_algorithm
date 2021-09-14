import sys
input = sys.stdin.readline

dic = {}


n = int(input())
for _ in range(n):
    person, log = map(str,input().split())
    
    if log == 'enter':
        dic[person] = 'enter'

    if log == 'leave':
        del dic[person]

res = sorted(dic.keys(), reverse=True)

for i in res:
    print(i)
