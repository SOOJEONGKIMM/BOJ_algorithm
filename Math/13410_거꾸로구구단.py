#13410_거꾸로 구구단
a, b= map(int,input().split())
inv=[]
for i in range(1, b+1):
    inv.append(int(str(i*a)[::-1]))
print(inv)
print(max(inv))
