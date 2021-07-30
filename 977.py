"""
Solution 1 查找最大的数值按次插入数组，最终逆序输出
"""


class Solution1(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            left_ = nums[left] ** 2
            right_ = nums[right] ** 2
            if left_ > right_:
                res.append(left_)
                left += 1
            else:
                res.append(right_)
                right -= 1

        return res[::-1]


"""
Solution 2 使用最小的正序输出
"""


class Solution2(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        min_index = None
        minimum = float('inf')
        for index, num in enumerate(nums):
            if num < minimum:
                min_index = index
                minimum = num
        left = right = min_index
        # flag =
        while left != -1 or right != len(nums):
            if left != -1:
                left_ = nums[left] ** 2
            else:
                left_ = nums[0] ** 2
            if right != len(nums):
                right_ = nums[right] ** 2
            else:
                right_ = nums[-1] ** 2
            if left_ < right_:
                if left != -1:
                    left -= 1
                    res.append(left_)
            else:
                if right != len(nums):
                    right += 1
                    res.append(right_)

        return res


if __name__ == '__main__':
    soul = Solution2()
    print(soul.sortedSquares([1, 3, 5, 6]))
