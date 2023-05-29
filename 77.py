def combine_new(start,end,num):
    if num ==1: #choose 1
        return [[x] for x in list(range(start, end + 1))]
    elif end -start +1 == num: # maybe choose more
        return [list(range(start,end+1))]
    elif end -start +1 - num > 0:
        res = []
        for i in range(end -start +1 - num+1):
            res.extend([start+i]+ item for item in combine_new(start+1+i,end,num-1))
        return res

import copy

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        def combine_inner(start):
            if len(temp) == k:
                res.append(copy.deepcopy(temp) )
                return
            for i in range(start,n+1):
                temp.append(i)
                combine_inner(i+1)
                temp.pop()
            return
        combine_inner(1)
        return res


if __name__ == '__main__':
    soul = Solution()
    print(soul.combine(4,3))