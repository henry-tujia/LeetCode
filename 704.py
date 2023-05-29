"""
Solution 1
使用前后指针，进行操作
"""


class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while True:
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1
            else:
                if nums[start] == target:
                    return start
                if nums[end] == target:
                    return end
                if nums[start] < target:
                    start += 1
                if nums[end] > target:
                    end -= 1


"""
Solution 2 使用二分查找来操作
"""


class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return search_true(nums, 0, len(nums) - 1, target)


def search_true(nums, left, right,  target):
    mid = int((left + right) / 2)
    if nums[mid] == target:
        return mid
    else:
        if mid == left:
            return -1
        if nums[mid] > target:
            return search_true(nums, left, mid - 1, target)
        if nums[mid] < target:
            return search_true(nums, mid + 1, right, target)


from typing import List
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


if __name__ == '__main__':
    soul = Solution3()
    print(soul.search([-1,0,3,5,9,12], 9))
