#1546_평균
N = int(input())
scores = list(map(int,input().split()))
max_ = max(scores)

new_=[]
for i in scores:
    new_.append(i/max_*100)
print(sum(new_)/N)
