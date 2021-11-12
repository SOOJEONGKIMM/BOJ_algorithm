#11286_절댓값 힙
import heapq
N = int(input())
arr=[]
for _ in range(N):
    x=int(input())
    if x!=0:
        heapq.heappush(arr, (abs(x), x))
    else:
        try:
            print(heapq.heappop(arr)[1])
        except:
            print(0)
    
