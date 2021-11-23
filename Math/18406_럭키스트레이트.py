#18406_럭키스트레이트
a = str(input())

length = len(a)

half = length//2
if sum([int(i) for i in a[:half]]) == sum([int(i) for i in a[half:]]):
    print("LUCKY")
else:
    print("READY")
                                       
