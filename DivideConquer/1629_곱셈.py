#1629_곱셈
a,b,c=map(int,input().split())

'''
수학의 분배법칙 => 분할정복
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
'''
def mul(a,b):
    if b==1:
        return a%c
    elif b%2==0:
        muldiv = mul(a,b//2)
        return (muldiv * muldiv) % c
    elif b%2!=0:
        muldiv = mul(a,b//2)
        return (muldiv * muldiv * a) % c


print(mul(a,b))
