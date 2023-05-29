import collections
from binarytree import build


class Solution(object):
    def flatten(self, root):
        def flatten_inner(root):
            if not root:
                return None
            flatten_left = flatten_inner(root.left)
            flatten_right = flatten_inner(root.right)
            root.left = None
            root.right = flatten_left
            p = root
            while p.right:
                p = p.right
            p.right = flatten_right

            return root
        return flatten_inner(root)


if __name__ == '__main__':
    tree_new = build(
        [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    print(tree_new)
    soul = Solution()

    print(soul.flatten(tree_new))
