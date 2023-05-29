
from typing import List
import copy


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        temp_target = 0
        candidates.sort()

        def combinationSum2_inner(start):
            nonlocal temp_target
            
            if temp_target > target:
                return
            if temp_target == target:
                res.append(copy.deepcopy(temp))
            
            for i in range(start, len(candidates)):
                if i> start and candidates[i-1] == candidates[i]:
                    continue
            
                temp.append(candidates[i])
                temp_target += candidates[i]
                combinationSum2_inner(i+1)
                temp.pop()
                temp_target -= candidates[i]

        combinationSum2_inner(0)
        return res


if __name__ == '__main__':
    soul = Solution()
    print(soul.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27))
