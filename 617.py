# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
新建节点来建立二叉树
"""

def newMerge(root1, root2):
    if root1 is None and root2 is None:
        return
    if root1 is None:
        return TreeNode(root2.val)
    elif root2 is None:
        return root1
    else:
        return TreeNode(root1.val + root2.val,root1.left,root1.right)


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged

