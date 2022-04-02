#1297_TV크기
import math
d,h,w = map(int, input().split())
one_b = (d**2 / (h**2 + w**2))**0.5
print(int(h*one_b), end=" ")
print(int(w*one_b))
