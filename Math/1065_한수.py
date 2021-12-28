#1065_한수
N=int(input())
hansu=0
for i in range(1,N+1):
    if i<100:
        hansu+=1
        #한자리 두자리는 모두 한수(무조건 등차수열 성립)
    else:
        nums=list(map(int, str(i)))
        if nums[2]-nums[1]==nums[1]-nums[0]:
            hansu+=1

print(hansu)
        
