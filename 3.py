class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        max_size = 0
        size_of_window = 0
        window = []

        for i in range(len(s)):
            if s[i] not in window:
                window.append(s[i])
                size_of_window += 1
            else:
                index = window.index(s[i])
                window.append(s[i])
                window = window[index+1:]
                size_of_window = len(window)
            max_size = max(max_size, size_of_window)

        return max_size


if __name__ == '__main__':
    soul = Solution()
    s = "aabaab!bb"
    print(soul.lengthOfLongestSubstring(s))
    # print(s)
