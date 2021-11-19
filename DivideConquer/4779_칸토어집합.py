import sys

for i in sys.stdin:
    tmp='-'

    for j in range(int(i)):
        tmp=tmp+' '*len(tmp)+tmp
    print(tmp)
