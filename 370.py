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
        self.pres[left] += num
        if right < len(self.nums)-1:
            self.pres[right+1] -= num
    def get_nums(self):
        self.construct_nums()
        return self.nums
if __name__ == "__main__":

    solu  =Solution(5)
    for update in [[1,3,2],[2,4,3],[0,2,-2]]:
        solu.update(*update)
        print(solu.get_nums())
    # pass

