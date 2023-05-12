#9935_문자열폭발_
string = str(input())
exp = str(input())
stack = []
for i in range(len(string)):
    stack.append(string[i])
   # print(stack, stack[-len(exp):])
    if exp==''.join(stack[-len(exp):]):
        for j in range(len(exp)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
        
