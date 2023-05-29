class ListNode():
    def __init__(self, val, next=None):
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


class Solution():
    def splitNodeList(self, head, x):
        p = head
        p_high = ListNode(0)
        p_low = ListNode(0)
        new_head = p_low
        mew_head_ = p_high
        while p:
            if p.val < x:
                p_low.next = p
                p_low = p_low.next
            else:
                p_high.next = p
                p_high = p_high.next
            p = p.next
        p_low.next = mew_head_.next
        return new_head.next

class Solution2():
    def splitNodeList(self, head,x):
        head_low = ListNode(-1)
        low_p = head_low
        head_high = ListNode(-1)
        high_p = head_high
        p = head
        while p is not None:
            if p.val < x:
                low_p.next = p
                low_p = low_p.next
            else:
                high_p.next = p
                high_p = high_p.next
            p = p.next
        low_p.next = head_high.next
        return head_low.next



if __name__ == "__main__":
    solu = Solution()
    head = create_linked_list([1, 5, 8, 4, 5, 1, 2, 9, 7])
    new_head = solu.splitNodeList(head, 7)
    print(print_linked_list(new_head))
