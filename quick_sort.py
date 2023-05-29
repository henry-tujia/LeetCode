import random

class Solution():
    def sort(self,nums):
        def partiton(start,end):
            p = random.randint(start,end-1)
            slow = []
            fast = []
            for index,num in enumerate(nums[start:end]):
                if index+start == p:
                    continue
                if num < nums[p]:
                    slow.append(num)
                else:
                    fast.append(num)
            temp = slow+[nums[p]]+fast
            for i in range(start,end):
                nums[i] = temp[i-start]
            print(start,end,p,nums)
            return start+len(slow)

        def sort_inner(start,end):
            if start >= end -1:
                return
            mid = partiton(start,end)
            sort_inner(start, mid)
            sort_inner(mid+1, end)
        sort_inner(0, len(nums))
        return nums

if __name__ == '__main__':
    soul = Solution()
    print(soul.sort([4,7,5,1,2,9,6,45,12,78,0]))