#1786_찾기(KMP알고리즘)
import sys
def getPi():
    m=len(p)
    j=0
    pi=[0 for i in range(0,len(p))] #kmptable
    for i in range(1,m):
        while j>0 and p[i]!=p[j]:#같지 않을때 
            j= pi[j-1]#이전의 맞는부분으로 돌아가서 다시 비교 
        if (p[i]==p[j]):#같으면
            j=j+1#j를 증가시키고 
            pi[i]=j#테이블갱신
    print(pi)
    return pi


def kmp(pi):
    
    j=0
    res=[]
    count=0
    for i in range(len(t)):
        while j>0 and t[i]!=p[j]:#같지않을때
            j=pi[j-1]#이전의 맞은 부분에 돌아가서 다시 비교 
        if t[i]==p[j]:#같으면
            if j==len(p)-1:
                count+=1#개수 추가 
                res.append(i-len(p)+2)#위치 추가 
                j=pi[j]#위치 옮겨주고 다시 탐색 
            else:#j를 늘려줌 
                j+=1
    print(count)
    for i in res:
        print(i)
        
    

t=sys.stdin.readline().split('\n')[0]
p=sys.stdin.readline().split('\n')[0]

kmp(getPi())

