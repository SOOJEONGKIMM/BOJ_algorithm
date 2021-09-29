#1448_삼각형 만들기
import sys
input = sys.stdin.readline

N = int(input())

straw=[]
for _ in range(N):
    straw.append(int(input()))

straw.sort(reverse=True)


#세 변 중 가장 긴 변의 길이 < 두 변의 길이 합

res=0
for i in range(len(straw)-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        res = straw[i] + straw[i+1] + straw[i+2]
        break
    else:
        res=-1

print(res)
