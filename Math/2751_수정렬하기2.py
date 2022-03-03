#2751_수정렬하기2
n=int(input())
su=[]
for _ in range(n):
    su.append(int(input()))
su=sorted(su)

for i in su:
    print(i, end='\n')
