




# class Solution(object):
#     def permute(self, nums):
#         def dfs(nums):
#             if not nums:
#                 return []
#             elif len(nums) ==1:
#                 return [[x] for x in nums]
#             else:
#                 res = []
#                 for item in nums:
#                     for _ in dfs([x for x in nums if x != item]):
#                         res.append([item]+_)
#                 return res
#         return dfs(nums)


# class Solution:
#     def permute(self, nums):
#         def permute_out(nums):
#             if len(nums) == 0:
#                 return []
#             if len(nums) == 1:
#                 return [nums]
#             res = []
#             for index,num in enumerate(nums):
#                 temp = permute_out([x for x in nums if x != num])
#                 # if isinstance(temp[0] , list):
#                 res+=[[num]+x for x in temp]
#                 # else:
#                 #     res.append([num]+temp)
#             # for i in range(len(nums)):
                 
#             return res
        
#         return permute_out(nums)

import copy
# class Solution:
#     def permute(self, nums):
#         used = [False]*len(nums)
#         res = []
#         temp  =[]

#         def permute_out():
#             if len(temp) == len(nums):
#                 res.append(copy.deepcopy(temp))
#                 return temp

#             for index,num in enumerate(nums):
#                 if used[index]:
#                     continue
#                 used[index] = True
#                 temp.append(num)
#                 permute_out()
#                 used[index] = False
#                 temp.pop()
            
#             return res

#         permute_out()
        
#         return res

class Solution:
    def permute(self, nums):
        res = []
        temp = []
        used = [False]*len(nums)

        def permute_out():
            if len(temp) == len(nums):
                res.append(copy.deepcopy(temp))
                return
            
            for index,num in enumerate(nums):
                if used[index]:
                    continue
                used[index] = True
                temp.append(num)
                permute_out()
                used[index] = False
                temp.pop()

        permute_out()
        return res

if __name__ == '__main__':
    soul = Solution()
    print(soul.permute([1,7,5]))