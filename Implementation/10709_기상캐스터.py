#10709_기상캐스터

H, W = map(int, input().split())

Wstring = []
for _ in range(H):
    Wstring.append(list(input()))

sky=[[-1]*W for _ in range(1,H+1)]

cnt=W
for k in range(0,W+1):
    for i in range(H):
        for j in range(W):
            if k==0:
                if Wstring[i][j]=='c':
                    sky[i][j]=0
            if k > 0:
                if i>-1 and j-1>-1:  
                    if sky[i][j-1]==k-1 and sky[i][j]!=0:                        
                        sky[i][j]=k
                
for i in range(H):
    for j in range(W):
        print(str(sky[i][j]), end=' ')
    print()
        
