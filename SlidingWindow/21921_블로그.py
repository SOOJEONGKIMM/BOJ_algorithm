#21921_블로그
#슬라이딩 윈도우 
n, x = map(int, input().split())

visit=list(map(int,input().split()))
if max(visit)==0:
    print("SAD")
else:
    value = sum(visit[:x])
    max_value = value
    max_cnt=1
    for i in range(x, n):
        value += visit[i]
        value -= visit[i-x]

        

        if value>max_value:
            max_value=value
            max_cnt=1
        elif value==max_value:
            max_cnt+=1
    print(max_value)
    print(max_cnt)
