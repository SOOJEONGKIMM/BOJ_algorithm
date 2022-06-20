#7568_덩치.py
n=int(input())
dongchi=[]
for i in range(n):
	dongchi.append(list(map(int,input().split())))

for i in dongchi:
	rank=1
	for j in dongchi:
		if i[0]<j[0] and i[1]<j[1]:
			rank+=1
	print(rank)

			
	
