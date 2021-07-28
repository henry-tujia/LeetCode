# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

"""
Solution 1 尝试二分查找，递归形式
"""


def isBadVersion(version):
    if version > 4:
        return True
    else:
        return False


def search(versions, start):
    if versions == 1:
        return start+versions
    mid = versions // 2
    mid_bad = isBadVersion(mid+start)
    mid_backward_bad = isBadVersion(mid - 1+start)
    if mid_bad and not mid_backward_bad:
        return start + mid
    if mid_bad:
        return search(versions - mid, start)
    else:
        return search(versions - mid, mid+start)


class Solution1(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return search(n, 0)


if __name__ == '__main__':
    soul = Solution1()
    print(soul.firstBadVersion(5))
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

"""
Solution 1 尝试二分查找，递归形式
"""


def isBadVersion(version):
    if version > 4:
        return True
    else:
        return False


def search(versions, start):
    if versions == 1:
        return start+versions
    mid = versions // 2
    mid_bad = isBadVersion(mid+start)
    mid_backward_bad = isBadVersion(mid - 1+start)
    if mid_bad and not mid_backward_bad:
        return start + mid
    if mid_bad:
        return search(versions - mid, start)
    else:
        return search(versions - mid, mid+start)


class Solution1(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return search(n, 0)


if __name__ == '__main__':
    soul = Solution1()
    print(soul.firstBadVersion(5))
