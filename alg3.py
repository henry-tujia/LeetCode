#

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#

# 找出并返回满足条件且不重复的三元组

# @param nums int整型一维数组 包含n个整数的数组nums

# @param target int整型 目标值

# @return int整型二维数组
#
import itertools
import sys


def threeSum(nums, target: int):
    import copy
    nums_old = copy.deepcopy(nums)
    nums.sort()
    pos = {}
    for index, k in enumerate(nums_old):
        if k in pos:
            pos[k].append(index)
        else:
            pos[k] = [index]
    res = {}

    def two_sum(nums, target, c_index):
        left = c_index+1
        right = len(nums)-1
        res = []
        while left < right:
            temp = nums[left]+nums[right]
            if temp == target:
                res.append([left, right])
                left += 1
                right -= 1
                while nums[left] == nums[left-1]:
                    left += 1
                while nums[right] == nums[right+1]:
                    right -= 1
            elif temp < target:
                left += 1
                while nums[left] == nums[left-1]:
                    left += 1
            else:
                right -= 1
                while nums[right] == nums[right+1]:
                    right -= 1
        return res

    for c_index in range(len(nums)):
        if nums[c_index] in res:
            continue
        temp_res = two_sum(nums, target-nums[c_index], c_index)
        c_res = []
        for temp in temp_res:
            c_res.append([nums[x] for x in temp])
        res[nums[c_index]] = c_res
    indexes = []
    for c_val in res:
        if len(res[c_val]):
            c_indexes = pos[c_val]
            for a_val, b_val in res[c_val]:
                a_indexes = pos[a_val]
                b_indexes = pos[b_val]
                for item in itertools.product(c_indexes, a_indexes, b_indexes):
                    item = sorted(item)
                    indexes.append(item)

    return sorted(indexes)


content = input()
content = content.replace(']', '').replace('[', '')
nums = [int(x) for x in content.split(',')]

print(threeSum(nums[:-1], nums[-1]))
