import sys
from collections import deque 
t = int(input())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    im = list(map(int, sys.stdin.readline().strip().split()))
    im = [(v,idx) for idx,v in enumerate(im)]
    cnt=0
    print(im)
    while True:
	if max(im)[0]==im[0][0]:
	    cnt+=1
	    if im[0][1]==m:
		print(cnt)
		break 
	    else:
		im.pop(0)
	else:
	    im.append(im.pop(0))
	  
