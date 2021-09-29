#2659_십자카드 문제
import sys
input = sys.stdin.readline


order = [0,1,2,3]*4

def clkk(clknum):
    clk=list(map(int,str(clknum)))
    for i in range(4):
        newclknum = int(clk[order[i+1]]*1000 + clk[order[i+2]]*100 + clk[order[i+3]]*10 + clk[order[i]])
        if clknum > newclknum:
            clknum = newclknum
    return clknum

clknum = clkk(int(''.join(input().split())))


cnt=0
for i in range(1111, clknum+1):
    check_zero=list(map(int,str(i)))
    if 0 not in check_zero:
        if clkk(i)==i:
            cnt += 1
print(cnt)

     
   
