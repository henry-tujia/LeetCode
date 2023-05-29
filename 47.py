from typing import List
import copy

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        used = [False]*len(nums)
        current = -1

        def permuteUnique_inner():
            nonlocal current
            if len(temp) == len(nums):
                res.append(copy.deepcopy(temp))
            for i,num in enumerate(nums):
                if used[i]:
                    continue
                if i>1 and nums[i-1] == num and not used[i-1]:
                    continue
                used[i] = True
                temp.append(num)
                permuteUnique_inner()
                temp.pop()
                used[i]=False

        permuteUnique_inner()
        return res

if __name__ == '__main__':
    soul = Solution()
    print(soul.permuteUnique([1,2,2,3]))