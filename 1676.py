from binarytree import build2

class Solution():
    def find_LCA(self,root,nums):
        def find_LCA_inner(root):
            if not root: return None
            if root.val in nums: return root
            left = find_LCA_inner(root.left)
            right = find_LCA_inner(root.right)

            return root if left and right else left or right
        res = find_LCA_inner(root)
        return res

if __name__ == '__main__':
    soul = Solution()
    tree = build2([0,1,2,4,5,6,7])
    print(tree)
    print(soul.find_LCA(tree, [2,7,6,1]))