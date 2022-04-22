#1911_흙길보수하기
n,l=map(int,input().split())
pool = [list(map(int, input().split())) for _ in range(n)]

pool.sort(key=lambda x: x[0])
plank = pool[0][0]
total_count = 0
for start, end in pool:
    if plank > end:
        continue
    elif plank < start:
        plank = start
    dist = end - plank
    remainder = 1
    if dist % l == 0:
        remainder = 0
    count = dist // l + remainder
    plank += count * l
    total_count += count
print(total_count)  
