#19944_뉴비의기준은뭘까?
n,m=map(int,input().split())

if m==1 or m==2:
    print("NEWBIE!")
elif m!=1 and m!=2 and m<=n:
    print("OLDBIE!")
else:
    print("TLE!")
