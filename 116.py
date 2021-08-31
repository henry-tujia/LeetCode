# Definition for a Node.
import collections
from tree_new import BinaryTree


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return

        visit = collections.deque()
        visit.append(root)
        cur = -1

        while visit:
            target = visit.popleft()
            cur += 1
            if (cur+2) & (cur + 1) != 0  and visit:
                target.next = visit[0]
            for kid in [target.left, target.right]:
                if kid is not None:
                    visit.append(kid)
        return root


if __name__ == '__main__':
    tree_new = BinaryTree(
        [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    soul = Solution()

    print(soul.connect(tree_new.root()))
