#10162_전자레인지
import sys
input = sys.stdin.readline
T = int(input())

# A B C: 5*60 1*60 10
A = 5*60
B = 60
C = 10

A_ = T // A
B_ = (T%A) // B
C_ = (T%A%B) // C

if A_*A + B_*B + C_*C != T:
    print(-1)
else:
    print(A_,B_, C_)
