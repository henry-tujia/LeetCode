# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while True:
            if fast.next == NULL:
                return slow
            if fast.next.next == NULL:
                return slow.next
            fast = fast.next.next
            slow = slow.next
            