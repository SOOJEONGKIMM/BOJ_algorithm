#2078_무한이진트리
a,b=map(int,input().split())
l=0
r=0
while a>1 and b>1:
    if a>b:
        l+=a//b
        a%=b
        
    else:
        r+=b//a
        b%=a
    print('a,b',a,b)
    print('l,r',l,r)
l+=a-1
r+=b-1
print(l,r)
        
