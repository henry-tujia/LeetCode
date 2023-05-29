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
    def reverseAreaList(self, head: ListNode, left: int, right: int) -> ListNode:
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
        left -= 1
        p_left = None
        right -= 1
        p_right = None

        left_low = left -1
        p_left_low = None
        right_high = right + 1
        p_right_high = None

        for i in range(right_high):
            if i == left -1:
                p_left_low = p
            if i== right + 1:
                p_right_high = p
            if i >= left:
                q = p
                p = p.next
                r = p.next
                p.next = q
        p_left_low.next = p_right
        p_left
        return head

    def reverseAreaList2(self, head: ListNode, left: int, right: int):

        def reverseAreaList_innrt(root):
            if root.next is None:
                return root
            last = reverseAreaList_innrt(root.next)
            root.next.next = root
            root.next = None

            return last

        p = head
        len_head = 0
        while p.next:
            p = p.next    
            len_head += 1

        head_need_left = head
        for _ in range(left):
            if _ == 0:
                continue
            head_need_left = head_need_left.next
        
        last_right = reverseAreaList_innrt(head_need_left.next)
        head_need_left.next = last_right

        # print(print_linked_list(head))

        head_need_right = last_right
        for _ in range(len_head-right):
            if _ == 0:
                continue
            head_need_right = head_need_right.next
        
        last_left = reverseAreaList_innrt(head_need_right.next)

        head_need_right.next = last_left

        # print(print_linked_list(head))

        last = reverseAreaList_innrt(last_right)

        head_need_left.next = last

        # print(print_linked_list(head))
        
        return head
        
        




if __name__ == "__main__":
    solu = Solution()
    head = create_linked_list([1,5,8,4,5])
    new_head = solu.reverseAreaList2(head,2,3)
    print(print_linked_list(new_head))