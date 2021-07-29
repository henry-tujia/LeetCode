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
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
        return left


"""
Solution2 二分查找
"""


class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        else:
            if nums[left] < target:
                return left + 1
            else:
                return left


"""
Solution 3 二分查找的优化版本
"""


class Solution3(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid+1
            if nums[mid] > target:
                right = mid -1
        return left


if __name__ == '__main__':
    soul = Solution3()
    print(soul.searchInsert([1, 3, 5, 6], 7))
