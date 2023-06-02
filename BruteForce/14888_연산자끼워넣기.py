
#14888_연산자끼워넣기
from itertools import permutations
n=int(input())
a=list(map(int,input().split()))

op_num = list(map(int,input().split()))#+-*%
op_list=['+','-','*','%']
op=[]

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum = -1e9
minimum = 1e9

def solve():
    global maximum
    global minimum

    for case in permutations(op, n-1):
        total = a[0]
     
        for r in range(1,n):
            if case[r-1]=='+':
                total+=a[r]
            elif case[r-1]=='-':
                total-=a[r]
            elif case[r-1]=='*':
                total*=a[r]
            elif case[r-1]=='%':
                total=int(total/a[r])
       
        if total>maximum:
            maximum = total
        if total<minimum:
            minimum = total

    
                
        

solve()
print(maximum)
print(minimum)
