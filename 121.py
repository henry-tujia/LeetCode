class Solution():
    def max_profit(self,prices):
        dp = [list(range(2)) for _ in prices]


        for i,_ in enumerate(prices):
            if i == 0:
                dp[0][1] = -float('inf')
                dp[0][0] = 0
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], -prices[i-1])

        return dp[-1][0]


if __name__ == '__main__':
    solu = Solution()
    print(solu.max_profit([7,1,5,3,6,4]))


