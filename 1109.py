class Solution():
    def __init__(self,length):
        self.nums = [0]*length
        self.pres = self.construct_pre_sums()
    def construct_pre_sums(self):
        pre = [0]*len(self.nums)
        for index, num in enumerate(self.nums):
            if index == 0:
                pre[index] = num
                continue
            pre[index] = self.nums[index]-self.nums[index-1]
        return pre
    def construct_nums(self):
        for index,num in enumerate(self.pres):
            if index == 0:
                self.nums[index] = num
                continue
            self.nums[index] = self.nums[index-1]+self.pres[index]
    def update(self,left,right,num):
        self.pres[left-1] += num
        if right-1 < len(self.nums)-1:
            self.pres[right] -= num
    def get_nums(self):
        self.construct_nums()
        return self.nums

if __name__ == '__main__':
    solu = Solution(5)

    for update in [[1,2,10],[2,3,20],[2,5,25]]:
        solu.update(*update)
    print(solu.get_nums())