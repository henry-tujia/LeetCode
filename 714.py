class Solution():
    def max_profit(self,prices,fee):
        a = 0
        b = -float('inf')

        for price in prices:
            temp_b = max(a-price, b)
            temp_a = max(a,b+price-fee)
            a = temp_a
            b = temp_b
        return a


if __name__ == '__main__':
    solu = Solution()
    print(solu.max_profit([1,3,2,8,4,9],2))