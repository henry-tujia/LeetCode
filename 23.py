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
    def mergeKLists(self, lists):
        K = len(lists)
        head = ListNode(0)
        p = head
        k_heads = lists[:]

        while any([k_head is not None for k_head in k_heads]):
            min = float('inf')
            temp = None
            for k_head in k_heads:
                # k_head = k_heads[i]
                if k_head is None:
                    continue
                if k_head.val <= min:
                    temp = k_head
                    min = k_head.val
                    # k_head = k_head.next

            for i in range(len(k_heads)):
                k_head = k_heads[i]
                if k_head is temp:
                    k_heads[i] = k_head.next
            p.next = temp
            p = p.next

        return head.next


class Solution2():
    def mergeKLists(self, heads):
        head = ListNode(-1)
        heads_vaild = [x for x in heads if x is not None]
        q = head
        while any(x for x in heads_vaild if x is not None):
            temp = None
            temp_id = -1
            for i, head_inner in enumerate(heads_vaild):
                if head_inner is None:
                    continue
                if temp is None:
                    temp = head_inner
                    temp_id = i
                    continue
                if head_inner.val < temp.val:
                    temp = head_inner
                    temp_id = i
            q.next = temp
            q = q.next
            if heads_vaild[temp_id] is None:
                continue
            heads_vaild[temp_id] = heads_vaild[temp_id].next
        return head.next


if __name__ == "__main__":
    solu = Solution2()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    heads = [create_linked_list(item) for item in lists]
    # print(any([k_head is not None for k_head in heads]))
    new_head = solu.mergeKLists(heads)
    print(print_linked_list(new_head))
