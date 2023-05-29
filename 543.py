# Definition for a Node.
import collections
from tree_new import BinaryTree


class Solution():
    def get_path(self, root):
        def get_path_inner(root):
            if root is None:
                return 0
            depth_left = get_path_inner(root.left)
            depth_right = get_path_inner(root.right)

            return depth_left+depth_right+1

        return get_path_inner(root)


if __name__ == "__main__":
    solu = Solution()
    tree_new = BinaryTree([-1, 0, 1, 2])
    print(solu.get_path(tree_new.root()))
