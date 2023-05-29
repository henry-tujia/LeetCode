
from typing import List
import copy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def subsetsWithDup_inner(start):
            res.append(copy.deepcopy(temp))

            for i in range(start, len(nums)):
                if i>start and nums[i-1] == nums[i]:
                    continue
                temp.append(nums[i])
                subsetsWithDup_inner(i + 1)
                temp.pop()
        subsetsWithDup_inner(0)
        return res


if __name__ == '__main__':
    soul = Solution()
    print(soul.subsetsWithDup([1,7,7]))
