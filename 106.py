class Tree_Node():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def construct_tree(self,afterorder,inorder):
        def construct_tree_inner(afterorder,inorder):
            if len(afterorder)==0:
                return None
            if len(afterorder)==1:
                return Tree_Node(afterorder[-1], None, None)
            root_val = afterorder[-1]
            root_id_in = inorder.index(root_val)
            left_tree = construct_tree_inner(afterorder[:root_id_in], inorder[:root_id_in])
            right_tree = construct_tree_inner(afterorder[root_id_in:-1], inorder[root_id_in+1:])
            root = Tree_Node(root_val,left_tree,right_tree)
            return root
        return construct_tree_inner(afterorder,inorder)


if __name__ == '__main__':
    solu = Solution()
    node = solu.construct_tree([9,15,7,20,3],[9,3,15,20,7])
    print('ok')
