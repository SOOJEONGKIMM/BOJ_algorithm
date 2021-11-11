#5052_전화번호목록
import sys
inp=sys.stdin.readline
nums=[]
T=int(input())
ans=[]
def compare(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] in nums[i+1][0:len(nums[i])]:
            print("NO")
            return False
    print("YES")
    return True
for _ in range(T):
    N=int(input())
    for _ in range(N):
        nums.append(inp().strip())
    compare(nums)
    nums.clear()


