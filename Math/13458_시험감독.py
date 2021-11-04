#13458_시험감독
N=int(input())
A=list(map(int, input().split()))
B, C = map(int, input().split())

gam=0

for i in range(N):
    if A[i]>0:
        A[i] -= B
        gam += 1

    if A[i]>0:
        gam += int(A[i]/C)
        if A[i]%C > 0:
            gam+=1
            

print(gam)

        
