
import sys
from collections import Counter
a = sys.stdin.readline().rstrip()
d = Counter(a)
s=""
for k, v in d.items():
    if v%2==1:
      if len(s)>0:
          print("I'm Sorry Hansoo")
          break
      s=k
ans=''
for k,v in sorted(d.items()):
    ans+=k*(v//2)
ans+= s + ans[::-1]
print(ans)
