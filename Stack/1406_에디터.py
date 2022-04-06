#1406_에디터
from sys import stdin
s=list(stdin.readline().strip())
res=[]
num=int(input())
cursor=len(s)
for _ in range(num):
    ctrl=list(map(str,input().split()))

    if ctrl[0]=='P':
        s.append(ctrl[1])
 
    elif ctrl[0]=='L':
        if s:
            res.append(s.pop())        
        else: continue
    elif ctrl[0]=='D':
        if res:
            s.append(res.pop())
        else:continue
    elif ctrl[0]=='B':
        if s:
            s.pop()
        else: continue
    print(s, res)


print(''.join(s + list(reversed(res))))

