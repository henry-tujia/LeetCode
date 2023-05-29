from binarytree import build

class Solution():
    def is_BST(self,root):
        def is_BST_inner(root,max_node,min_node):
            if root is None:
                return True
            if min_node and min_node.val > root.val:
                return False
            if max_node and max_node.val < root.val:
                return False
            return is_BST_inner(root.left, root, min_node) and is_BST_inner(root.right, max_node, root)
        return is_BST_inner(root,None, None)

if __name__ == '__main__':
    soul = Solution()
    tree = build([10,5,15,None,None,14,20])
    print(soul.is_BST(tree))
            