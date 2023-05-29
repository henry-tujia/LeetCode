class Tree_Node():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def find_max(nums):
    max_index,max_val = 0,-float('inf')
    for index,val in enumerate(nums):
        if val > max_val:
            max_val = val
            max_index = index
    return max_index,max_val

class Solution():
    def construct_tree(self,nodes):
        def construct_tree_node(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return Tree_Node(nums[0], None, None)
            max_index,max_val = find_max(nums)
            left_tree = construct_tree_node(nums[:max_index])
            right_tree = construct_tree_node(nums[max_index+1:])
            return Tree_Node(max_val, left_tree, right_tree)
        return construct_tree_node(nodes)

if __name__ == '__main__':
    solu = Solution()
    node = solu.construct_tree([3,2,1,6,0,5])
    print('ok')

