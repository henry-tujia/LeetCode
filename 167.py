class Solution:
    def twoSum(self, numbers, target):
        res = None
        left = 0
        right = len(numbers) - 1
        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                res = [left + 1, right + 1]
                break
            elif result < target:
                left += 1
            elif result > target:
                right -= 1
        return res


if __name__ == '__main__':
    soul = Solution()
    print(soul.twoSum([2, 7, 11, 15], 9))
