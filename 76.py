import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        valid = 0
        target = {k: 0 for k in t}
        for i in t:
            target[i] += 1
        windows = {k: 0 for k in t}

        left = 0
        right = 0
        start = 0
        length = len(s)
        while right < len(s):
            if s[right] in t:
                windows[s[right]] += 1
                if windows[s[right]] == target[s[right]]:
                    valid += 1
            while valid == len(target):
                if right - left < length:
                    length = right - left
                    start = left
                if s[left] in t:
                    if windows[s[left]] == target[s[left]]:
                        valid -= 1
                    windows[s[left]] -= 1
                left += 1
            right += 1

        return s[start:start+length+1] if length < len(s) else ""

    def minStr(self, s, t):
        import collections

        def check_dict(s,t):
            for key in t.keys():
                if key in s:
                    if s[key] < t[key]:
                        return False
                else:
                    return False
            return True

        left = 0
        right = 1
        t_dict = collections.Counter(t)
        res = s

        while right < len(s):
            right += 1

            sub_str = s[left:right]
            temp_dict = collections.Counter(sub_str)

            while check_dict(temp_dict, t_dict):
                if right - left < len(res):
                    res = s[left:right]
                left += 1
                sub_str = s[left:right]
                temp_dict = collections.Counter(sub_str)
        return res



if __name__ == '__main__':
    soul = Solution()
    print(soul.minStr(
        s="iquxdmafnmzwpvgvgieflwlybmpocprlflikeufebeohqqeykjwrif", t="iu"))
