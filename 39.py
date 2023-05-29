from typing import List
import copy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        temp_target = 0

        def combinationSum_inner(start):
            nonlocal temp_target
            if temp_target > target:
                return
            if temp_target == target:
                res.append(copy.deepcopy(temp))

            for index,num in enumerate(candidates[start:]):
                temp.append(num)
                temp_target += num
                combinationSum_inner(index+start)
                temp.pop()
                temp_target -= num
            
        combinationSum_inner(0)
        return res


if __name__ == '__main__':
    soul = Solution()
    print(soul.combinationSum([2], target = 1))