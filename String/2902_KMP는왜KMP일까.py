#2902_KMP는왜KMP일까?
kmp=list(map(str,input().split('-')))

res=''
for i in kmp:
    res+="".join(i[0])
print(res)
