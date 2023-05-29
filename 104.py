# Definition for a Node.
import collections
from tree_new import BinaryTree


def FindMaxDepth(root, depth):
    if root is None:
        return 0
    depth = max(FindMaxDepth(root.left, depth),
                FindMaxDepth(root.right, depth))+1

    return depth


def FindMaxDepth_Tree(root, depth):
    if root is None:
        return 0
    depth += 1
    depth_left = FindMaxDepth_Tree(root.left, depth=0)
    depth_right = FindMaxDepth_Tree(root.right, depth=0)

    depth += max(depth_left,depth_right)

    return depth
 

class Solution(object):
    def MaxDepth(self, root):
        return FindMaxDepth_Tree(root, 0)

def FindMaxDepth_Tree_2(root):
    if root is None:
        return 0
    return 1+max(FindMaxDepth_Tree_2(root.left),FindMaxDepth_Tree_2(root.right))


class Solution2():
    def  MaxDepth(self, root):
        return FindMaxDepth_Tree_2(root)
        # pass


if __name__ == '__main__':
    tree_new = BinaryTree([-1, 0, 1, 2])
    soul = Solution2()

    print(soul.MaxDepth(tree_new.root()))
