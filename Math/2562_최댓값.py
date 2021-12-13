#2562_최댓값
num=[]
for _ in range(9):
    num.append(int(input()))

maxnum = max(num)
index = num.index(maxnum)

print(maxnum)
print(index+1)
