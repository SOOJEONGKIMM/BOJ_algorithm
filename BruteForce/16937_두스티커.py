#16937_두스티커
h,w=map(int,input().split())
n=int(input())
rc=list(list(map(int,input().split())) for _ in range(n))

res=0
for i in range(n):
    for j in range(i+1, n):
        r1, c1 = rc[i]
        r2, c2 = rc[j]

         #둘다 회전x
        if (r1 + r2 <=h and max(c1,c2)<=w) or (max(r1,r2) <=h and c1+c2<=w):
            res=max(res, r1*c1 + r2*c2)
        #rc2 회전
        if (r1 + c2 <=h and max(r1,c2)<=w) or (max(r1,c2) <=h and r1+c2<=w):
            res=max(res, r1*c1 + r2*c2)
        #rc1 회전
        if (c1 + r2 <=h and max(r1,c2)<=w) or (max(c1,r2) <=h and r1+c2<=w):
            res=max(res, r1*c1 + r2*c2)
        #둘다 회전
        if (c1 + c2 <=h and max(r1,r2)<=w) or (max(c1,c2) <=h and r1+r2<=w):
            res=max(res, r1*c1 + r2*c2)

        
print(res)
