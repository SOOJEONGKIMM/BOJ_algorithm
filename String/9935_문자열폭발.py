#9935_문자열 폭발
import sys
string = str(sys.stdin.readline().rstrip())
explode = list(sys.stdin.readline().rstrip())

len_ex = len(explode)
stack=[]
for i in string:
    stack.append(i)
    if i==explode[-1] and explode==stack[-len_ex:]:
        for _ in range(len_ex):
            stack.pop()

res = ''.join(stack)
if len(res)==0:
    print("FRULA")
else:
    print(res)
