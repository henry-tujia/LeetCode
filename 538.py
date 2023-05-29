import collections

class tree_node():
    def __init__(self,val,left = None,right = None,size = 0):
        self.val = val
        self.left = left
        self.right = right
        self.size = size

class Solution():
    def construct_tree(self,nums):
        current_layer_nodes = collections.deque()
        for num in nums:
            if num is not None:
                current_layer_nodes.append(tree_node(num))
            else:
                current_layer_nodes.append(None)
        self.root = current_layer_nodes.popleft()
        last_layer_nodes = collections.deque()
        last_layer_nodes.append(self.root)
        while current_layer_nodes:
            node = last_layer_nodes.popleft()
            if node is None:
                continue
            if current_layer_nodes:
                node.left = current_layer_nodes.popleft()
                last_layer_nodes.append(node.left)
            if current_layer_nodes:
                node.right = current_layer_nodes.popleft()
                last_layer_nodes.append(node.right)
    def get_size(self):
        temp = 0
        def get_size_inner(root):
            nonlocal temp
            if root is None:
                return 0
            get_size_inner(root.left)
            temp += 1
            root.size = temp
            get_size_inner(root.right)

        get_size_inner(self.root)
    def get_count(self,k):
        count = 0
        res = None
        def get_count_inner(root):
            nonlocal count
            nonlocal res
            if root is None:
                return
            if k < root.size:
                get_count_inner(root.left)
            elif k == root.size:
                res = root
            else:
                get_count_inner(root.right)
        get_count_inner(self.root)
        return res
            
if __name__ == '__main__':
    soul = Solution()
    soul.construct_tree([5,3,6,2,4,None,None,1])
    soul.get_size()
    print(soul.get_count(2))