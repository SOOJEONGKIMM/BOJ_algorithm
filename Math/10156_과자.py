#10156_과자
k,n,m=map(int,input().split())

res = k*n - m

if res < 0:
    print(0)
else:
    print(res)
