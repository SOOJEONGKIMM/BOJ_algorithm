import sys
input = sys.stdin.readline
N = int(input())

num_list = []

num_list=map(int, input().split())

prime_cnt=0

for i in num_list:
    #에리토스테네스의 체
    flag = 0
    if i > 1:
        for j in range(2, i//2+1):    
            if (i%j == 0):
                flag += 1 #배수는 배열에서 제거 
        if flag == 0:
            prime_cnt+=1 #배수가 아님 
print(prime_cnt)
