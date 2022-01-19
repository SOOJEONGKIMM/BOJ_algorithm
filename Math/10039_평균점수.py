#10039_평균점수
iphone=[]
for i in range(5):
    score=int(input())
    if score >=40:
        iphone.append(score)
    else:
        iphone.append(40)

print(sum(iphone)//5)
