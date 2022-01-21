#5904_Moo 게임

#s(d)=s(d-1)+'m'+'o'*(d+2)+s(d-1)
#총 3가지 파트로 구성 

n=int(input())
def moo(n,degree,pre_len):
    #s(d-1)길이는 s(d)길이에서 가운데부분길이 뺀 후 2로 나눈것
    first = (pre_len-degree)//2
    if n <= first: return moo(n, degree-1, first)
    elif n > first+degree: return moo(n-first-degree,degree-1,first)
    else: return 'o' if n-first-1 else 'm'
    
pre_len=3
degree=0
while n>pre_len:
    degree+=1
    pre_len = pre_len*2+degree+2+1

print(moo(n,degree+2+1,pre_len))
    
