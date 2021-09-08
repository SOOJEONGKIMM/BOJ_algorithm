#14888
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().strip())
num_list = list(map(int, input().strip().split()))
op_list = list(map(int, input().strip().split()))

max_result = -1000000000
min_result = 1000000000

operator = ['+','-','*','/']
op_per = []
for i in range(4):
    for j in range(op_list[i]):
        op_per.append(operator[i])
        
op_per = list(set(permutations(op_per, len(op_per))))



for j in op_per:
    result = num_list[0]
    for i in range(0,N-1):
        #+
        if j[i]=='+':
            result = result + num_list[i+1]
            op_list[0]-=1
        #-
        elif j[i]=='-':
            result = result - num_list[i+1]
            op_list[1]-=1
        #x
        elif j[i]=='*':
            result = result * num_list[i+1]
            op_list[2]-=1
        #/
        elif j[i]=='/':
            if result<0:
                result = -(-result // num_list[i+1])
            else:
                result = result // num_list[i+1]
            op_list[3]-=1
        if i==N-2:
            max_result = max(max_result, result)
            min_result = min(min_result, result) 
   
print(max_result)
print(min_result)
    
