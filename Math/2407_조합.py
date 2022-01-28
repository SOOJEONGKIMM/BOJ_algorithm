#2407_조합
import math
n,m=map(int,input().split())
up=math.factorial(n)//math.factorial(n-m)
down=math.factorial(m)
print(up//down)
