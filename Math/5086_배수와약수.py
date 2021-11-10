#5086_배수와약수
while(True):
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        if b%a==0:
            print("factor")
        elif a%b==0:
            print("multiple")
        else:
            print("neither")
