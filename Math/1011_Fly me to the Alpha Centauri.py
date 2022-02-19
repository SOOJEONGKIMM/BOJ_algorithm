#1011_Fly me to the Alpha Centauri
import math
T=int(input())
for _ in range(T):
    x,y=map(int,input().split())

    distance = y-x
    count=0
    root = math.floor(math.sqrt(distance))
    print(root)
    max_square = root ** 2
    max_root = math.sqrt(max_square)
    print(max_square, max_root)
    if distance > max_square + max_root:
        count = 2*root+1
    elif distance == max_square:
        count = 2*max_root-1
    elif distance <= max_square + max_root:
        count = 2*root
    
    print(int(count))
        
        
