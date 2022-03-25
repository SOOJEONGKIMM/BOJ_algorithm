#4153_직각삼각형
while 1:
    tri = list(map(int,input().split()))
    if sum(tri)==0:
        break
    heru = max(tri)
    tri.remove(heru)
    if heru**2 == tri[0]**2 + tri[1]**2:
        print('right')
    else:
        print('wrong')
