#5622_다이얼
import sys
input = sys.stdin.readline

word = input()

alph = ['_','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

res=0
for i in range(len(word)):
    idx=0
    for j in alph:
        idx+=1
        if word[i] in j:
            res+=idx+1
print(res)
