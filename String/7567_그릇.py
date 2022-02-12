dish=list(map(str,input().rstrip()))
res=0
for i in range(len(dish)):
    if i==0:
        res+=10
    elif dish[i]==dish[i-1]:
        res+=5
    else:
        res+=10
print(res)
