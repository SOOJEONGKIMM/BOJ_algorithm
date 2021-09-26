#2331 반복수열
import sys
input = sys.stdin.readline

A, P = map(int, input().split())

perm = [A]

while True:
    res = 0
    A=perm[-1]

    while(A!=0):
        res += ((A%10)**P)    
        A = A//10
        
    if res in perm:
        fin = perm.index(res)
        perm = perm[:perm.index(res)]
        break   
    perm.append(res)
    A=res

print(fin)
