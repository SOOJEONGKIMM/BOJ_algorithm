#1543_문서검색

search = input()

find = input()

cur=0
cnt=0
while cur < len(search):
    if find in search[cur:cur+len(find)]:
        cnt+=1
        cur+=len(find)
    else:              
        cur+=1
print(cnt)
