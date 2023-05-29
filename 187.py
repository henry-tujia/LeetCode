class Solution():
    def find_repeated_substring(self, string):
        nums = []
        for char in string:
            if char == 'A':
                nums.append(0)
            elif char == 'G':
                nums.append(1)
            elif char == 'C':
                nums.append(2)
            elif char == 'T':
                nums.append(3)
        N = 5
        R = 4
        value = 0

        max_val = R**(N-1)

        value_set = set()
        res = []

        left,right = 0,0

        while right < len(string):
            value  = value*R + nums[right]
            right += 1

            if right - left  == N:
                if value in value_set:
                    res.append(string[left:right])
                else:
                    value_set.add(value)
                value -= max_val*nums[left]
                left += 1
        return res
 

if __name__ == '__main__':
    solu = Solution()
    s = "AACTAAACTAGTC"

    print(solu.find_repeated_substring(s))  