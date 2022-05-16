#10814_나이순정렬
n=int(input())
online=[]
for _ in range(n):
    online.append(input().split())

online.sort(key=lambda x:int(x[0]))

for i in range(n):
    print(online[i][0], online[i][1])
