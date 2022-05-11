#10773_제로

K=int(input())
jang = []

for _ in range(K):
    a=int(input())
    if a==0:
        jang.pop()
    else:
        jang.append(a)

print(sum(jang))
