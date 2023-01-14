class Node:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

#   Tree like this below
#              4
#         2          6
#      1     3    5     7
#
#   Their id is
#              0
#         1          2
#      3     4    5     6


# Convert Sorted List to ADT
node6 = Node(7, None)
node5 = Node(5, node6)
node4 = Node(3, node5)
node3 = Node(1, node4)
node2 = Node(6, node3)
node1 = Node(2, node2)
node0 = Node(4, node1)

root = node0


max_index = 6

def get_parent(index):
    if index > max_index:
        print("Error, please input the correct index")
        return

    if index == 0:
        print("The node does not have parent")
        return

    ans_index = int((index - 1) / 2)
    i = 0
    root_now = root
    while i < ans_index:
        i += 1
        root_now = root_now.next

    print("The node's parent is ", root_now.key)

def get_left_children(index):
    if index > max_index:
        print("Error, please input the correct index")
        return

    ans_index = index * 2 + 1
    if ans_index > max_index:
        print("The node does not have left children")
        return

    i = 0
    root_now = root
    while i < ans_index:
        i += 1
        root_now = root_now.next

    print("The node's left children is ", root_now.key)

def get_right_children(index):
    if index > max_index:
        print("Error, please input the correct index")
        return

    ans_index = index * 2 + 2
    if ans_index > max_index:
        print("The node does not have right children")
        return

    i = 0
    root_now = root
    while i < ans_index:
        i += 1
        root_now = root_now.next


    print("The node's right children is ", root_now.key)

def solve(index):
    get_parent(index)
    get_left_children(index)
    get_right_children(index)

solve(2)

from collections import deque
import datetime


# 存储最小堆节点的类
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# 插入key
def insert(root, key):
    # 如果根为空，创建一个新节点并返回
    if root is None:
        return TreeNode(key)

    # 如果key小于根节点，插入左子树
    if key < root.key:
        root.left = insert(root.left, key)

    # 如果key大于根节点，插入右子树
    else:
        root.right = insert(root.right, key)

    return root


# 顺序遍历
def printLevelOrderTraversal(root):
    # 空树
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        n = len(q)
        while n > 0:
            n = n - 1
            front = q.popleft()
            print(front.key, end=' ')
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        print()


# 从构造的队列中构建完整的二叉树
def construct(keys):
    # 存储父节点
    q = deque()

    # 初始化根节点
    root = TreeNode(keys.pop())

    # 根节点入队
    q.append(root)

    # 循环处理
    while keys:

        # 前节点出队
        parent = q.popleft()

        # 用next key分配父节点的左孩子
        parent.left = TreeNode(keys.pop())

        # 入队左子节点
        q.append(parent.left)

        # 如果key存在
        if keys:
            # 用next key分配父节点的右孩子
            parent.right = TreeNode(keys.pop())

            # 入右孩子队
            q.append(parent.right)

    # 返回根节点
    return root


# 中序遍历
# 入队 按顺序
def inorder(root, keys):
    if root is None:
        return

    inorder(root.right, keys)
    keys.append(root.key)
    inorder(root.left, keys)


# 函數將 BST 转换为最小堆而不使用
# 任意輔助空間
def convert(root):
    # 存储逆序遍历
    keys = []
    inorder(root, keys)

    # 从queue排列建造完全二叉树
    root = construct(keys)
    return root

def delMin(root):
    return root.key

if __name__ == '__main__':

    keys = [5, 3, 2, 4, 8, 10]

    ''' Construct the following BST
               5
             /   \
            /     \
           3       8
          / \       \
         /   \       \
        2     4      10
    '''

    # 记录开始时间
    starttime = datetime.datetime.now()


    for i in range(1000000):
        root = None
        for key in keys:
            root = insert(root, key)

        root = convert(root)

    # 记录结束时间

    root = None
    for key in keys:
        root = insert(root, key)

    root = convert(root)
    printLevelOrderTraversal(root)

    endtime = datetime.datetime.now()

    # 打印
    print("建树 1000000 次的时间为:")
    print(str((endtime - starttime).seconds) + "s")

    min_now = delMin(root)

    new_keys = []
    for key in keys:
        if key == min_now:
            continue
        new_keys.append(key)

    root = None
    for key in new_keys:
        root = insert(root, key)

    root = convert(root)
    printLevelOrderTraversal(root)
