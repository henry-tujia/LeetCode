"""
Solution 1 Wrong!排序而非相对顺序

"""


def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] == 0:
                right -= 1
            if nums[right] > nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        reverse(nums, 0, right - 1)


class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        int_index, zero_index = 0, 0
        while zero_index < len(nums):
            if nums[zero_index] != 0:
                zero_index += 1
                if zero_index == len(nums):
                    break
            else:
                int_index += 1
                if int_index == len(nums):
                    break
            if nums[zero_index] == 0 and nums[int_index] != 0 and zero_index < int_index:
                nums[int_index], nums[zero_index] = nums[zero_index], nums[int_index]


if __name__ == '__main__':
    nums = [1, 0]
    sulo = Solution2()
    sulo.moveZeroes(nums)
    print(nums)
