#10773
import sys
k=int(sys.stdin.readline())
j=[]
for _ in range(k):
	
	new=int(sys.stdin.readline())
	if new==0:
		j.pop()
	else:
		j.append(new)

print(sum(j))
	

