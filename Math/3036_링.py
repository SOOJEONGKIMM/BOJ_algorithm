#3036_링
import math
n=int(input())
ring = list(map(int,input().split()))
for i in range(1,n):
    g=math.gcd(ring[0],ring[i])
    print('{0}/{1}'.format(ring[0]//g,ring[i]//g))
    
