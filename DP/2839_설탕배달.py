#2839

n=int(input())
res=0
while n>=0:
	five = n // 5
	leftover = n - five*5
	if leftover==0:
		res+=five
		print(res)
		break
	elif leftover > 0:
		#three = leftover // 3
		n -= 3
		res+=1

if n < 0:
	print(-1)
	
