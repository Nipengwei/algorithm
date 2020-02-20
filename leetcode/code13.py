# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head

        cur_node = head
        start_node = None
        for _ in range(m-1):
            start_node = cur_node
            cur_node = cur_node.next
        
        pre_node = start_node
        rev_end_node = cur_node

        for _ in range(n-m+1):
            nxt_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = nxt_node
        
        if start_node:
            start_node.next = pre_node
        else:
            head = pre_node
        rev_end_node.next = cur_node

        return head