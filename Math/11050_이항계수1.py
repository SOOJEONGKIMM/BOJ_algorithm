#11050_이항계수1
from math import factorial
n,k=map(int,input().split())

print(factorial(n)//(factorial(n-k)*factorial(k)))
