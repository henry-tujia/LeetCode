# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binarytree import build
import queue

# class Solution:
#     def minDepth(self, root) -> int:
#         if root is None:
#             return 0
#         q = queue.Queue()
#         visited = set()
#         depth = 1

#         q.put(root)

#         while q:
#             for _ in range(q.qsize()):
#                 node = q.get()
#                 if node in visited:
#                     continue
#                 visited.add(node)
#                 if node.left is None and node.right is None:
#                     return depth
#                 if node.left is not None:
#                     q.put(node.left)
#                 if node.right is not None:
#                     q.put(node.right)
#             depth += 1

class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        def minDepth_inner(root):
            if root.left is None and root.right is None:
                return 1
            if root.left is not None:
                depth_left = minDepth_inner(root.left)
            if root.right is not None:
                depth_right = minDepth_inner(root.right)
            
            return 1 + min(depth_left,depth_right)
        
        return minDepth_inner(root)


if __name__ == '__main__':
    solu = Solution()
    root = build([2,None,3,None,4,None,5,None,6])
    print(root)
    print(solu.minDepth(root))