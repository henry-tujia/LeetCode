class Solution:
    def coinChange(self, coins, amount) -> int:

        return coinChange_out(coins, amount)

    def coinChange2(self, coins, amount):
        if amount == 0:
            return 0
        if amount < coins[0]:
            return -1
        res = [0]*(amount+1)
        for i in range(coins[0], amount+1):
            res[i] = 1+min(res[i-x] for x in coins if i-x >= 0)
        return res[-1]


def coinChange_out(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    temp = []
    for coin in coins:
        temp_res = coinChange_out(coins, amount-coin)
        if temp_res > -1:
            temp.append(temp_res)

    return min(temp)+1 if temp else -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.coinChange2([1, 2, 5], 11))
