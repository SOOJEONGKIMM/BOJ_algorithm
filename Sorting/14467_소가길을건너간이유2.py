#14467_소가길을건나간이유1
N=int(input())
index=[-1]*11
cnt=0
for _ in range(N):
    cow_num, cow_index= map(int, input().split())

    if index[cow_num]==-1:
        index[cow_num]=cow_index
    else:
        if index[cow_num]!=cow_index:
            cnt+=1
        index[cow_num]=cow_index   
print(cnt)
