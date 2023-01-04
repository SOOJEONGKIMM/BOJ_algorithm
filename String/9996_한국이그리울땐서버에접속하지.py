#정규표현식으로 패턴 반환
import re, sys
n=int(input())
f,l=sys.stdin.readline().rstrip().split('*')
pt = re.compile(f+'.*'+l+'+')
for _ in range(n):
    file=sys.stdin.readline().rstrip()
    a = pt.search(file)
    if a and a.group() == file:
	    print("DA")
    else:
	    print("NE")
    
