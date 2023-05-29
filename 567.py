"""
可以使用统计次数来进行比较
"""


# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         # 统计 s1 中每个字符出现的次数
#         counter1 = collections.Counter(s1)
#         N = len(s2)
#         # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
#         left = 0
#         right = len(s1) - 1
#         # 统计窗口s2[left, right - 1]内的元素出现的次数
#         counter2 = collections.Counter(s2[0:right])
#         while right < N:
#             # 把 right 位置的元素放到 counter2 中
#             counter2[s2[right]] += 1
#             # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
#             if counter1 == counter2:
#                 return True
#             # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
#             counter2[s2[left]] -= 1
#             # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
#             if counter2[s2[left]] == 0:
#                 del counter2[s2[left]]
#             # 窗口向右移动
#             left += 1
#             right += 1
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s2) == len(s1) and s2 != s1:
        #     return False
        target,source = (s2,s1) if len(s1)> len(s2) else (s1,s2)
        dict_target = {k :0 for k in target}
        dict_source = {k :0 for k in target}
        for s in target:
            dict_target[s] += 1
        left = 0
        right = 0
        valid = 0
        while right < len(target):
            if source[right] in dict_target:
                dict_source[source[right]] += 1
                if dict_source[source[right]] == dict_target[source[right]]:
                    valid += 1
            while valid == len(dict_target):
                if source[right] in dict_target:
                    dict_source[source[right]] -= 1
                    if dict_source[source[right]] == dict_target[source[right]]:
                        valid -= 1
                    left += 1
            right += 1
        return right-left+1 == len(target)
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        import collections

        s1_dict = collections.Counter(s1)

        left = 0
        right = len(s1)

        while right < len(s2)+1:
            sub_str = s2[left:right]
            sub_dict = collections.Counter(sub_str)
            if sub_dict == s1_dict:
                return True
            right += 1
            left += 1
        return False

if __name__ == '__main__':
    soul = Solution()

    print(soul.checkInclusion2("ab", "bacd"))
