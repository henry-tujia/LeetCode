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

class Solution():
    def flip_k_linknodes(self, head, k):
        def flip_top_k(root, target):
            if root.next is None or root.next is target:
                return root
            last = flip_top_k(root.next, target)
            root.next.next = root
            root.next = target
            return last

        p = head
        for  _ in range(k):
            p = p.next

        return flip_top_k(head,p)
if __name__ == "__main__":
    solu = Solution()
    head = create_linked_list([1,5,8,4,5,6,7])
    new_head = solu.flip_k_linknodes(head,2)
    print(print_linked_list(new_head))
