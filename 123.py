class Solution():
    def max_profit(self,prices):
        dp = [-float('inf')]*5
        dp[-2] = 0
        dp_temp = dp

        for price in prices:
            dp_temp[0] = max(dp[0],dp[2]+price)
            dp_temp[1] = max(dp[1],dp[4]+price)
            dp_temp[2] = max(dp[2],dp[1]-price)
            dp_temp[3] = dp[3]
            dp_temp[4] = max(dp[3]-price,dp[4])

            dp = dp_temp
        return dp[0]


if __name__ == '__main__':
    solu = Solution()
    print(solu.max_profit([3,3,5,0,0,3,1,4]))