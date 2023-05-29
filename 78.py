import copy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        temp = []

        def subsets_inner(start):
            res.append(copy.deepcopy(temp))
            for i in range(start, len(nums)):
                temp.extend([nums[i]])
                subsets_inner(i+1)
                temp.pop()
        
        subsets_inner(0)
        return res

        




if __name__ == '__main__':
    soul = Solution()
    print(soul.subsets([4,3,1]))