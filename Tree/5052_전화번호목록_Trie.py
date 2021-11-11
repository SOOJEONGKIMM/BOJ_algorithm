#5052_전화번호목록_Trie
import sys
import math

class Node(object):
    def __init__(self, flag):
        self.flag = flag #문자열의 종료를 알리는 flag (문자열을저장) 
        self.child = {}
        self.check = False

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur_node = self.root

        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = Node(char)
            cur_node = cur_node.child[char]
        cur_node.flag = string

    def search(self, string):
        cur_node = self.root

        for char in string:
            if char in cur_node.child:
                cur_node = cur_node.child[char]

        if cur_node.child:
            return False
        else:
            return True
    def starts_with(self, prefix):
        cur_node = self.root
        words=[]

        for p in prefix:
            if p in cur_node.child:
                cur_node = cur_node.child[p]
            else:
                return Node

        cur_node = [cur_node]
        next_node = []
        while True:
            for node in cur_node:
                if node.flag:
                    words.append(node.flag)
                next_node.extend(list(node.child.values()))
            if len(next_node)!=0:
                cur_node = next_node
                next_node = []
            else:
                break

        return words


inp=sys.stdin.readline

T=int(input())
trie = Trie()
for _ in range(T):
    N=int(input())
    nums_list=[]
    for _ in range(N):
        nums=input().rstrip()
        trie.insert(nums)
        nums_list.append(nums)
    res=True
    nums_list.sort()

    for nums in nums_list:
        if not trie.search(nums):
            res=False
            break
    if res:
        print("YES")
    else:
        print("NO")
    nums_list.clear()
