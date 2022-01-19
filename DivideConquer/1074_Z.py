#1074_Z
n,r,c=map(int,input().split())

def sol(n,r,c):
    if n==0:
        return 0
    return 2*(r%2)+(c%2) + 4*(sol(n-1,r//2,c//2))

print(sol(n,r,c))
