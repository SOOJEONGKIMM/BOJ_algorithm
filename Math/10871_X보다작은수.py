#10871_X보다작은수
n, x = map(int,input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i]<x:
        print(a[i],end=" ")
