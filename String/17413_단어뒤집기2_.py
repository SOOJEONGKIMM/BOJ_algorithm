import sys
s = sys.stdin.readline().rstrip()
tmp=[]
ans=""
flag=0
for i in s:
    tmp.append(i)
    if i==' ' and flag==0:
        tmp=tmp[:-1]
        ans+=''.join(tmp[::-1])+' '
        tmp=[]
    elif i=='<':
        flag=1
        tmp=tmp[:-1]
        ans+=''.join(tmp[::-1])
        ans+='<'
        tmp=[]
    elif i=='>':
        flag=0
        tmp=tmp[:-1]
        ans+=''.join(tmp)
        ans+='>'
        tmp=[]
	

ans+=''.join(tmp[::-1])
print(ans)
