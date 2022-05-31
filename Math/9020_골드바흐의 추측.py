#9020_골드바흐의 추측
t=int(input())
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,int(a**0.5)+1):
    if(a%i==0):
      return False
  return True

array = [1 for i in range(t+1)]
for _ in range(t):
    a=int(input())
    b=int(a/2)
    c=int(a/2)
    for _ in range(int(a)):
        if isPrime(b) and isPrime(c):
            print(b,c)
            break
            
        else:
            b=b-1
            c=c+1
            
