from binarytree import build2

class Solution():
    def find_LCA(self,root,val0,val1):
        targets = [val0,val1]
        def find_LCA_inner(root):
            if not root or not len(targets): return None
            if root.val in targets: 
                targets.pop(targets.index(root.val))
                return root
            left = find_LCA_inner(root.left)
            right = find_LCA_inner(root.right)
            return root if left and right else left or right

        res = find_LCA_inner(root)
        return None if len(targets) else res

if __name__ == '__main__':
    soul = Solution()
    tree = build2([0,1,2,4,5,6,7])
    print(tree)
    print(soul.find_LCA(tree, 2, 8))