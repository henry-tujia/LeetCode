"""
Solution 1 使用分次旋转方法
"""


def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0,  k - 1)
        reverse(nums, k, len(nums) - 1)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    sulo = Solution()
    sulo.rotate(nums, 3)
    print(nums)
