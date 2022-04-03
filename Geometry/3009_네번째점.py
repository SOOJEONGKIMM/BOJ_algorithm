#3009_네번째점
rectx=[]
recty=[]
for _ in range(3):
    x,y = map(int,input().split())
    rectx.append(x)
    recty.append(y)
resx, resy = 0, 0
for i in range(3):
    if rectx.count(rectx[i])==1:
        resx=rectx[i]
    if recty.count(recty[i])==1:
        resy=recty[i]
print(resx, end=" ")
print(resy)
