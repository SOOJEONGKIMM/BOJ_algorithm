#1003_피보나치함수

T=int(input())
for _ in range(T):
    zero, one = 1, 0
    tmp=0
    for _ in range(int(input())):
        tmp=one
        one=zero+one
        zero=tmp
    print(zero, one)
