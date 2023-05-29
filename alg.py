# def get_sum(target,nums):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         temp = nums[left]+nums[right]
#         if temp == target:
#             return (nums[left],nums[right])
#         elif temp < target:
#             left +=1
#         else:
#             right -= 1
#     return None


# nums = [1,4,5,6,9,10]
# target = 10

# print(get_sum(target, nums))


# def insert_item(nums,target):
#     left = 0
#     right = len(nums)-1
#     index = 0
#     for i in range(len(nums)):
#         if nums[i] > target:
#             index = i
#             break
#     return nums[:index]+[target]+nums[index:]


def insert_item(nums,target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right)//2
        # if nums[mid] == target:
        #     index = mid
        #     break
        if nums[mid] > target:
            right = mid -1
        else:
            left = mid +1
    return nums[:left]+[target]+nums[left:] if left !=len(nums)-1 else nums+[target]

nums = [1,2,4,5]
target = 6

print(insert_item(nums, target))