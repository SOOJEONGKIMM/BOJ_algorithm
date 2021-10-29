#9466
T=int(input())

for _ in range(T):
    n = int(input())
    num = [0] + list(map(int, input().split()))
    visited=[0]*(n+1)
    res=0
    for i in range(1, n+1):
        if visited[i]:
            continue
        index = i
        circle = [index]
        visited[index]=1
        while (1):
            last = num[index]
            if visited[last]:
                break
            index = last
            circle.append(index)
            visited[index]=1

        if circle and last in circle:
            res += len(circle[circle.index(last):])
    print(n - res)
