from binarytree import build2
from itertools import product
class Solution():
    def count_SBT(self, nums):
        temp_res = {}

        def count_BST_inners(start, end):
            if start == end:
                return [None]
            if (start, end) in temp_res:
                return temp_res[(start, end)]
            res = []
            for root_index in range(start, end):
                left_count = count_BST_inners(start, root_index)
                right_count = count_BST_inners(root_index+1, end)
                for left,right in product(left_count, right_count):
                    root = build2([nums[root_index]])
                    root.left = left
                    root.right = right
                    res.append(root)
            temp_res[(start, end)] = res
            return res
        res = count_BST_inners(0, len(nums))
        return res


if __name__ == '__main__':
    soul = Solution()
    for node in soul.count_SBT(list(range(5))):
        print(node)
