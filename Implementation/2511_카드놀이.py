#2511_카드놀이
import sys
A=list(map(int,sys.stdin.readline().strip().split()))
B=list(map(int,sys.stdin.readline().strip().split()))
Ares=Bres=0
if A==B:
    print(10,10)
    print('D')
else:
    for i in range(10):

        if A[i]>B[i]:
            Ares+=3
            win='A'
        elif A[i]<B[i]:
            Bres+=3
            win='B'
        else:
            Ares+=1
            Bres+=1
    print(Ares,Bres)
    if Ares==Bres:
        print(win)
    elif Ares>Bres:
        print('A')
    else:
        print('B')
