class Solution():
    def __init__(self,nums):
        self.nums = nums
        self.construct_pre_sums()
    def construct_pre_sums(self):
        pre = [0]
        pre.extend(pre[index] + num for index, num in enumerate(self.nums))
        self.pre_nums = pre
    def sum_target(self,left,right):
        return self.pre_nums[right+1] - self.pre_nums[left]

if __name__ == '__main__':
    input_0 = ["NumArray","sumRange","sumRange","sumRange"]
    input_1 = [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

    nums = input_1[0][0]

    res = [None]
    solu = Solution(nums)

    res.extend(solu.sum_target(*args) for args in input_1[1:])

    print(res)

