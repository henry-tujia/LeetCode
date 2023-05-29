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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy = ListNode(0, head)
        # first = head
        # second = dummy
        # for i in range(n):
        #     first = first.next

        # while first:
        #     first = first.next
        #     second = second.next

        # second.next = second.next.next
        # return dummy.next
        p = head
        p_fast = head

        for i in range(n+1):
            p_fast = p_fast.next

        while p_fast:
            p_fast = p_fast.next
            p = p.next

        if p.next:
            p.next = p.next.next
        else:
            p.next = None
        
        return head

if __name__ == "__main__":
    solu = Solution()
    head = create_linked_list([1,5,8,4,5,1,2,9,7])
    new_head = solu.removeNthFromEnd(head,2)
    print(print_linked_list(new_head))