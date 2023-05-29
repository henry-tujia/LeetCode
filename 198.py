from binarytree import build

class Solution():
    def max_profit(self,prices):
        a = 0
        b = -float('inf')

        for price in prices:
            temp_a = max(a,b)
            b = a+price
            a = temp_a

        return max(a,b)

    def max_profit_circle(self,prices):
        def max_profit_circle_inner(start,end):
            a = 0
            b = -float('inf')

            for price in prices[start:end]:
                temp_a = max(a,b)
                b = a+price
                a = temp_a
            return max(a,b)

    def max_profit_tree(self,prices):
        tree = build(prices)
        def max_profit_tree_inner(root,rob):
            if root is None:
                return 0
            left_val = max_profit_tree_inner(root.left, False)
            right_val = max_profit_tree_inner(root.right, False)
            if rob:
                return root.val + left_val + right_val
            left_val_ = max_profit_tree_inner(root.left, True)
            right_val_ = max_profit_tree_inner(root.right, True)
            return max(left_val,left_val_) + max(right_val,right_val_)
        
        temp_left = max_profit_tree_inner(tree,True)
        temp_right = max_profit_tree_inner(tree,False)

        return max(temp_left,temp_right)



if __name__ == '__main__':
    solu = Solution()
    print(solu.max_profit_tree([3,4,5,1,3,None,1]))