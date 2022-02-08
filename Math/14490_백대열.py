#14490_백대열
import sys
left, right = map(int, sys.stdin.readline().split(':'))
a=left
b=right
while left!=right:
    if left>right: left-=right
    else: right-=left #최대공약수 만들기_유클리드호제법 

print('{}:{}'.format(a//left, b//left))

