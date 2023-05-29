class Tree_Node():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def construct_tree(self,preorder,inorder):
        def construct_tree_inner(preorder,inorder):
            if len(preorder)==0:
                return None
            if len(preorder)==1:
                return Tree_Node(preorder[0], None, None)
            root_val = preorder[0]
            root_id_in = inorder.index(root_val)
            left_tree = construct_tree_inner(preorder[1:root_id_in+1], inorder[:root_id_in])
            right_tree = construct_tree_inner(preorder[root_id_in+1:], inorder[root_id_in+1:])
            root = Tree_Node(root_val,left_tree,right_tree)
            return root
        return construct_tree_inner(preorder,inorder)


if __name__ == '__main__':
    solu = Solution()
    node = solu.construct_tree([3,9,20,15,7],[9,3,15,20,7])
    print('ok')
