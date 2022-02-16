#1929_소수구하기

def isPrime(a):
    if a<2:
        return False
    for i in range(2, int(a**0.5)+1):
        if (a%i==0):
            return False
    return True

M,N = map(int, input().split())

for i in range(M, N+1):
    if(isPrime(i)):
        print(i)
