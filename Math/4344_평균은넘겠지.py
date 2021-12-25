#4344_평균은넘겠지
T=int(input())
for _ in range(T):
    st = list(map(int, input().split()))
    stnum=st[0]
    av = sum(st[1:])/stnum
    av_over=0
    for student in st[1:]:
        if student>av:
            av_over+=1
    print("{:.3f}%".format((av_over)/stnum*100),end="\n")
