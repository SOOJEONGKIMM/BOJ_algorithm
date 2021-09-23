#1100하얀칸
import sys
input = sys.stdin.readline

chess = []
white = [0,2,4,6]

horse=0
for i in range(8):
    chess.append(list(map(str,input())))

for i in range(8):  
    for j in range(8):
        if (i+j)%2==0:
            if chess[i][j]=='F':
                horse+=1

print(horse)

