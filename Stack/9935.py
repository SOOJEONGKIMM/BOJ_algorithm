#9935 문자열폭발
s = str(input()).rstrip()
explosion  = str(input()).rstrip()

stack = []
ex_len = len(explosion)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-ex_len:]) == explosion:
        for _ in range(ex_len):
            stack.pop()


if stack:
    print(''.join(stack))
else:
    print("FRULA")
               
