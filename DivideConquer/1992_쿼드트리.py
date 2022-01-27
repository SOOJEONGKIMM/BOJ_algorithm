
#1992_쿼드트리
n=int(input())
graph=[list(map(int,input())) for i in range(n)]
res=""
def quad(y,x,n):
    global res
    arr=graph[y][x]
    notsame=False
    for i in range(y,y+n):
        brk=False
        for j in range(x,x+n):
            if arr!=graph[i][j]:
                notsame=True
                brk=True
                break
        if brk==True:
            break
    if notsame==False:
        res+=str(graph[y][x])
    else:
        half = n // 2
        res+='('
        quad(y, x, half)
        quad(y, x + half, half)
        quad(y + half, x, half)
        quad(y + half, x + half, half)
        res+=')'
    
quad(0,0,n)

print(res)
