class Solution():
    def count_SBT(self, nums):
        temp_res = {}

        def count_BST_inners(start, end):
            if start == end:
                return 1
            if (start, end) in temp_res:
                return temp_res[(start, end)]
            res = 0
            for root_index in range(start, end):
                left_count = count_BST_inners(start, root_index)
                right_count = count_BST_inners(root_index+1, end)
                res += left_count*right_count
            temp_res[(start, end)] = res
            return res
        res = count_BST_inners(0, len(nums))
        return res


if __name__ == '__main__':
    soul = Solution()
    print(soul.count_SBT(list(range(3))))
