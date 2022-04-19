#2805_나무자르기
n,m=map(int,input().split())

tree = list(map(int,input().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start+end) //2

    leftover = 0

    for i in tree:
        if i>mid :
            leftover += i - mid

    if leftover >= m:
        start = mid +1
    else:
        end = mid -1
    print(start, end, mid)

print(end)
