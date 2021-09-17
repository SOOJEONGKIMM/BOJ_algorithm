import sys
input = sys.stdin.readline

S = input()

alph = list(range(97,123))

for i in alph:
    print(S.find(chr(i)), end=' ')
    
