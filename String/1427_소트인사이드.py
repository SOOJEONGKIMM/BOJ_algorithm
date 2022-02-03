#1427
num=int(input())
new_num=[]
for i in str(num):
    new_num.append(i)

new_num.sort(reverse=True)

print(''.join(new_num))
