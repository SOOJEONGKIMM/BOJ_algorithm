#트리 자식노드(낙엽)개수 구하기
#참고 백준 1068 1991번
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_binary_tree(arr):
    n = len(arr)
    if n == 0:
        return None

    root = Node(arr[0])
    queue = [root]
    i = 1

    while i < n:
        node = queue.pop(0)

        if i < n:
            node.left = Node(arr[i])
            queue.append(node.left)
            i += 1

        if i < n:
            node.right = Node(arr[i])
            queue.append(node.right)
            i += 1

    return root

def count_leaf_nodes(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    left_count = count_leaf_nodes(root.left)
    right_count = count_leaf_nodes(root.right)
    
    return left_count + right_count
def print_binary_tree(root):
    if root is None:
        return

    queue = [root]

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print()
# 주어진 리스트
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 이진 트리 생성
tree_root = construct_binary_tree(arr)
print_binary_tree(tree_root)
# 차수가 0인 노드 개수 계산
leaf_node_count = count_leaf_nodes(tree_root)

print("차수가 0인 노드 개수:", leaf_node_count)
