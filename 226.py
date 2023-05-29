from binarytree import build

class Solution(object):
    def flip(self,root):
        def flip_tree(root):
            if root is None:
                return None
            temp = flip_tree(root.left)
            root.left = flip_tree(root.right)
            root.right = temp
            return root
        return flip_tree(root)



if __name__ == '__main__':
    tree_new = build([-1, 0, 1, 2])
    print(tree_new)
    soul = Solution()

    print(soul.flip(tree_new))