#2884_알람시계
H, M = map(int, input().split())
if M > 44:
    print(H, M-45)
elif H==0:
    print(23, M+15)    
elif M <45:
    print(H-1, M+15) #ex) 40분 - 45 = 55분 

