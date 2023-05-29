class Solution():
    def sort(self,nums):
        left = 0
        right = len(nums)-1
        def merge(nums,left,mid,right):
            if nums[mid]<nums[mid+1]:
                return
            p_l = left
            p_right = mid+1
            temp = nums[left:right+1]
            p = left
            while p <= right:
                if p_l == mid+1:
                    nums[p] = temp[p_right]
                    p_right  += 1
                elif p_right == right+1:
                    nums[p] = temp[p_l]
                    p_l  += 1
                elif temp[p_l]< temp[p_right]:
                    nums[p] = temp[p_l]
                    p_l  += 1
                else:
                    nums[p] = temp[p_right]
                    p_right  += 1
                p += 1

        def sort_inner(nums,left,right):
            if right == left:
                return 
            mid = (left + right)//2
            sort_inner(nums, left, mid)
            sort_inner(nums, mid+1, right)
            merge(nums, left, mid,right)

        sort_inner(nums, left, right)
        return nums
        

if __name__ == '__main__':
    solu = Solution()
    print(solu.sort([1,4,2,3]))