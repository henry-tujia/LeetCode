class Solution():
    def compute(self, n):
        if n <= 2:
            return 1
        a = 1
        b = 1
        c = 0
        for _ in range(n-2):
            c = a+b
            a = b
            b = c

        return c

    def compute2(self, n):
        res = {}

        def compute2_inner(n):
            if n <= 2:
                return 1
            if n in res:
                return res[n]
            res_inner = compute2_inner(n-1)+compute2_inner(n-2)
            res[n] = res_inner
            return res_inner

        return compute2_inner(n)


if __name__ == '__main__':
    solu = Solution()
    print(solu.compute2(10))
