from binarytree import build

from binarytree import build
class Solution():
    def searchBST(self,root,target):
        res = None
        def searchBST_inners(root):
            nonlocal res
            if not root:
                return
            if root.val == target:
                res = root
            elif root.val > target:
                searchBST_inners(root.left)
            else:
                searchBST_inners(root.right)
        searchBST_inners(root)
        return res
    def insert_BST(self,root,target):
        def insert_BST_inners(root):
            if not root:
                return build([target])
            if root.val < target:
                root.right = insert_BST_inners(root.right)
            elif root.val > target:
                root.left = insert_BST_inners(root.left)
            return root
        root = insert_BST_inners(root)
        return root
    def delete_BST(self,root,target):
        def delete_BST_inners(root):
            if not root:
                return
            if root.val == target:
                if not root.right and not root.left:
                    root = None
                elif root.left:
                    if root.right:
                        p = root.left
                        while p.right:
                            p = p.right
                        p.right = root.right
                    root = root.left
                elif root.right:
                    root = root.right
            elif root.val < target:
                root.right = delete_BST_inners(root.right)
            else:
                root.left = delete_BST_inners(root.left)
            return root
        root = delete_BST_inners(root)
        return root
 
if __name__ == '__main__':
    soul = Solution()
    tree = build([10,5,15,None,None,14,20])
    print(tree)
    print(soul.delete_BST(tree, 5))
