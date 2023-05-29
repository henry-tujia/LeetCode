class Solution():
    def three_sum(self, nums):
        # a+b = -c
        nums.sort()

        total_res = set()

        def two_sum(nums, target):
            res = []
            slow = 0
            fast = len(nums)-1

            while slow < fast:
                temp_res = nums[slow] + nums[fast]
                if temp_res == target:
                    res.append([slow, fast])
                    for offset, num in enumerate(nums[slow:]):
                        if num != nums[slow]:
                            slow += offset
                            break
                    for offset, num in enumerate(nums[:fast+1][::-1]):
                        if num != nums[fast]:
                            fast -= offset
                            break
                elif temp_res < target:
                    for offset, num in enumerate(nums[slow:]):
                        if num != nums[slow]:
                            slow += offset
                            break
                else:
                    for offset, num in enumerate(nums[:fast+1][::-1]):
                        if num != nums[fast]:
                            fast -= offset
                            break
            return res
        for i, _ in enumerate(nums):
            if i<len(nums)-1 and _ == nums[i+1]:
                continue
            for res in [(nums[i],*x) for x in two_sum(nums[:i]+nums[i+1:], -nums[i]) if len(x)]:
                total_res.add(res)
        return total_res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    solu = Solution()

    print(solu.three_sum(nums))
