V = int(input())
vote = list(str(input()))

A = B = 0
for v in vote:
    if v == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif A == B:
    print('Tie')
else:
    print('B')
