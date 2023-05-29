class Solution():
    def max_profit(self,prices):
        a = 0
        b = -float('inf')

        for price in prices:
            temp_a = max(a-price, b)
            temp_b = max(b+price, a)
            b = temp_a
            a = temp_b
        return a

if __name__ == '__main__':
    solu = Solution()
    print(solu.max_profit([1,2,3,4,5]))