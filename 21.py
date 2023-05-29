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

# def merge(l1,l2):
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1

#     if l1.val <= l2.val:
#         p = l1
#         l1 = l1.next
#     else:
#         p = l2
#         l2 = l2.next

#     p.next = merge(l1, l2)

#     return p


def merge(l1,l2):
    head = ListNode(-1)
    # head = l1 if l1.val < l2.val else l2
    p = head
    while (l1 is not None) or (l2 is not None):
        if l2 is None:
            p.next = l1
            break
        if l1 is None:
            p.next = l2
            break
        if l1.val < l2.val:
            p.next = l1
            # head.next = p
            l1 = l1.next
        elif l1.val >= l2.val:
            p.next = l2
            # head.next = p
            l2 = l2.next
        p = p.next

        # p = l1 if l1.val < l2.val else l2
        # # head.next = p
        # p = p.next
    return head.next


class Solution2(object):
    def merge(self,l1,l2):
        head = ListNode(-1)
        q = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val :
                p = l1
                l1 = l1.next
            else:
                p = l2
                l2 = l2.next
            q.next = p
            q = q.next
        if l1 is None:
            q.next = l2
        elif l2 is None:
            q.next = l1

        return head.next







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
        
        return merge(l1,l2)
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         head = l2 if l2.val < l1.val else l1

#         merge(l1,l2)
#         return head



if __name__ == '__main__':
    soul = Solution2()
    l1 = create_linked_list([1,3,5,7,9,10])
    l2 = create_linked_list([2,4,6,7])

    print(print_linked_list(soul.merge(l1, l2)))
