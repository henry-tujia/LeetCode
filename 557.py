class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        reverse_words = [self.reverse(word) for word in words]
        return ' '.join(reverse_words)

    def reverse(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        s = ''.join(s)
        return s


if __name__ == '__main__':
    soul = Solution()
    s = "Let's take LeetCode contest"
    print(soul.reverseWords(s))
    # print(s)
