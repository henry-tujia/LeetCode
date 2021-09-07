class Solution(object):
    def permute(self, nums):
        def dfs(nums):
            if not nums:
                return []
            elif len(nums) ==1:
                return [[x] for x in nums]
            else:
                res = []
                for item in nums:
                    for _ in dfs([x for x in nums if x != item]):
                        res.append([item]+_)
                return res
        return dfs(nums)

if __name__ == '__main__':
    soul = Solution()
    print(soul.permute([1,21,3]))