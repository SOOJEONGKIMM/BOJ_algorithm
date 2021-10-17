#1316_그룹단어체커
N = int(input())

word=[]
cnt=N
for _ in range(N):
    word=input()
    for i in range(0, len(word)-1):            
        if word[i] in word[i+1:]:
            if word[i]!=word[i+1]:     
                cnt-=1
                continue
        
print(cnt)
