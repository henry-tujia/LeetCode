class Solution():
    def find_indexes(self, s, p):
        import collections
        left = 0
        right = len(p)
        res = []

        p_dict = collections.Counter(p)

        while right < len(s)+1:
            sub_str = s[left:right]
            sub_dict = collections.Counter(sub_str)
            if sub_dict == p_dict:
                res.append(left)
            left += 1
            right += 1

        return res

if __name__ == '__main__':
    s = 'cbaebabacd'
    p  = 'abc'
    solu = Solution()
    print(solu.find_indexes(s, p))
