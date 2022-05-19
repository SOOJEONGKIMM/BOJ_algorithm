#2920_음계
mm=list(map(int,input().split()))

if mm == sorted(mm):
    print('ascending')
elif mm== sorted(mm, reverse=True):
    print('descending')
else:
    print('mixed')


