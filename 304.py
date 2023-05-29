import itertools
class Solution():
    def __init__(self,nums):
        self.nums = nums
        self.construct_pre_sums()

    def construct_pre_sums(self):
        m = len(self.nums)
        n = len(self.nums[0])
        pre = [[0]*(n+1) for _ in range(m+1)]

        for j, i in itertools.product(range(1,m+1), range(1,n+1)):
            pre[j][i]= pre[j][i-1]+pre[j-1][i]-pre[j-1][i-1]+self.nums[j-1][i-1]
        self.pre_nums = pre
    def sumRange(self,m1,n1,m2,n2):
        return self.pre_nums[m2+1][n2+1]-self.pre_nums[m2+1][n1]-self.pre_nums[m1][n2+1]+self.pre_nums[m1][n1]

if __name__ == '__main__':
    nums = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    solu = Solution(nums)

    print(solu.sumRange(2,1,4,3))
