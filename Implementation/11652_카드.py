#11652:카드
import sys
input = sys.stdin.readline

N = int(input())
card=[]
for _ in range(N):
    card.append(int(input()))

cnt={}
for i in card:
    try: cnt[i]+=1
    except: cnt[i]=1

res = sorted(cnt.items(), key=(lambda x:(x[1],-x[0])), reverse=True)


print(res[0][0])
