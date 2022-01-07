#17204_죽음의게임
n, k = map(int, input().split())
nums=[]
for _ in range(n):
    nums.append(int(input()))


start=nums[0]
point_list=[]
for _ in range(n):
    point_list.append(start)
    nextt=nums[start]
    point_list.append(nextt)
    start=nums[nextt]

if k in point_list:
    print(point_list.index(k)+1)
else:
    print('-1')
