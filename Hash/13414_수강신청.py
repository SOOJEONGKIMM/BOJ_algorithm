#13414_수강신청
k,l = map(int,input().split())
num=dict()
for i in range(l):
    num[input()]=i    

num2 = sorted(num.items(), key=lambda x: x[1])

cnt=0
for i in num2:
    if cnt>=k:
        break
    cnt+=1
    print(i[0])
