#10813_공바꾸기
N, M = map(int, input().split())
basket = [ i+1 for i in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    basket[a-1],basket[b-1] = basket[b-1],basket[a-1]

print(*basket)
    
