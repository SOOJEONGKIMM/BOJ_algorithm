#25379_피하자
def is_even(x):
    if x % 2 ==0:
        return True
    else:
        return False

if __name__=="__main__":
    n=int(input())
    pairs = list(map(int,input().split()))

    even_left=0
    even_right=0
    
    #even to left
    tmp=0
    for i in pairs:
        if is_even(i):
            tmp+=1
        else:
            even_left+=tmp

    tmp=0
    pairs.reverse()

    for i in pairs:
        if is_even(i):
            tmp+=1
        else:
            even_right+=tmp

    print(min(even_left, even_right))
