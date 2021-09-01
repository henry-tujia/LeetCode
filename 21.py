# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

def merge(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val <= l2.val:
        p = l1
        l1 = l1.next
    else:
        p = l2
        l2 = l2.next

    p.next = merge(l1, l2)

    return p


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = l2 if l2.val < l1.val else l1

        merge(l1,l2)
        return head



if __name__ == '__main__':
    soul = Solution()
    l1 = create_linked_list([])
    l2 = create_linked_list([])

    print(print_linked_list(soul.mergeTwoLists(l1, l2)))
