#9093_단어뒤집기
t = int(input())

for _ in range(t):
    res=[]
    word = list(map(str, input().strip().split()))
    for  i in word:        
        print(i[::-1],end=' ')
    print()
