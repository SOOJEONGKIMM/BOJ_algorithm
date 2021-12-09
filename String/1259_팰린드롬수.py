#1259_팰린드롬수
while True:
    n=list(str(input()))
    if n==['0']:
        break
    backn=n[::-1]

    if n==backn:
        print('yes')
    else:
        print('no')
