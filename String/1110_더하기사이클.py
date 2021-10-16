#1110_더하기 사이클
n = int(input())
num=n
cnt = 0

while (1):
    ten = num // 10
    one = num % 10
    plus = (ten+one) % 10
    num = one*10 + plus

    cnt +=1

    if (num==n):
        break
print(cnt)
