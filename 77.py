def combine_new(start,end,num):
    if num ==1: #choose 1
        return [[x] for x in list(range(start, end + 1))]
    elif end -start +1 == num: # maybe choose more
        return [list(range(start,end+1))]
    elif end -start +1 - num > 0:
        res = []
        for i in range(end -start +1 - num+1):
            for item in combine_new(start+1+i,end,num-1):
                res.append([start+i]+ item)
        return res

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return combine_new(1,n,k)


if __name__ == '__main__':
    soul = Solution()
    print(soul.combine(4,3))