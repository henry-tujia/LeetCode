from binarytree import build

class Solution():
    def find_repeated_tree(self,root):
        res = {}
        
        def find_repeated_tree_inner(root):
            if root is None:
                return ""
            left_str = find_repeated_tree_inner(root.left)
            if len(left_str) > 0:
                left_str += ","
            right_str = find_repeated_tree_inner(root.right)
            if len(right_str) > 0:
                right_str = f",{right_str}"
            root_str = left_str + str(root.val) + right_str
            if root_str in res:
                res[root_str] += 1
                # res_final.append(root_str)
            else:
                res[root_str] = 1
            return root_str
        find_repeated_tree_inner(root) 
        res_final = [k for k,v in res.items() if v>1]
        return res_final

if __name__ == '__main__':
    solu = Solution()

    tree = build([1,2,3,4,None,2,4,None,None,None,None,4])
    node = solu.find_repeated_tree(tree)
    print(node) 