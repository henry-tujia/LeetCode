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


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        p_last = p
        p = p.next
        p_next = p.next
        # head.next = None
        while p is not None:
            p.next = p_last
            p_last = p
            p = p_next
            if p is None:
                break
            p_next = p.next
        head.next = None
        return p_last

if __name__ == '__main__':
    soul = Solution()
    l1 = create_linked_list([1,2,3,4,5])

    print(print_linked_list(soul.reverseList(l1)))