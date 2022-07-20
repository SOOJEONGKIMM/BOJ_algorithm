n=int(input())
num=[]
cnt = 1 
stack=[]
for _ in range(n):
	new = int(input())
	while cnt <= new:
		num.append(cnt)
		stack.append('+')
		cnt+=1
	if num[-1]==new:
		num.pop()
		stack.append('-')
	else:
		print('\nNO')
		exit(0)
for i in range(len(stack)):
	print(stack[i])
