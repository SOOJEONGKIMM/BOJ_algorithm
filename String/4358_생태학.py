import sys
from collections import defaultdict
trees = defaultdict(int)

n=0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
	    break
    trees[tree]+=1
    n+=1

tree_lst = list(trees.keys())
tree_lst.sort()
for tree in tree_lst:
    print('%s %.4f' %(tree, trees[tree]/n*100))
