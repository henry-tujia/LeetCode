class Solution():
    def max_profit(self,prices):
        a = 0
        b = -float('inf')
        c = -float('inf')

        for price in prices:
            temp_a = max(a,c)
            temp_b = max(a-price,b)
            temp_c = b+price

            a = temp_a
            b = temp_b
            c = temp_c
        return max(a,c)


if __name__ == '__main__':
    solu = Solution()
    print(solu.max_profit([1,2,3,0,2]))