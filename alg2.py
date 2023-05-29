import sys


# lines = "1 2 4 3".split()

n = 4

nums = "1 2 4 3".split()

# print(n,len(words))

used = [False]*n
temp_res = []
res = 0

exchanges = 0

def com_exchange(nums1,nums2):
    global exchanges

    if len(nums1) == 2 and nums1 != nums2:
        return 1

    samed = [nums1[x]== nums2[x] for x in range(len(nums1))]

    nums1_new = [nums1[x] for x in range(len(samed)) if not x]
    nums2_new = [nums2[x] for x in range(len(samed)) if not x]

    exchanges += com_exchange(nums1_new, nums2_new)
    

def is_corr(nums):
    temp = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if temp > 1:
                return False
            if nums[i] > nums[j]:
                temp += 1
    if temp == 1:
        return True
    return False


def get_res_inner(words):
    global res
    if len(temp_res) == n:
        if is_corr(temp_res):
            res += 1
            print(temp_res)
        return
    for i in range(len(words)):
        if used[i]:
            continue
        used[i] = True
        temp_res.append(words[i])
        get_res_inner(words)
        temp_res.pop()
        used[i] = False


def get_res(n, nums):
    if n != len(nums):
        return 0
    if n == 1:
        return 0
    get_res_inner(nums)
    return res


print(get_res(n, nums) % (10**9+7))

print(com_exchange([1,2,3],[2,3,1]))
