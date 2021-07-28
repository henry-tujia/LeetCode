"""
Solution 1 双向指针
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <=right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
        return left


if __name__ == '__main__':
    soul = Solution()
    print(soul.searchInsert([1,3,5,6], 7))
