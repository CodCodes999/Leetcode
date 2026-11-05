# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head = ListNode(0)
        cur_node = head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            col_sum = l1val+ l2val + carry
            carry = col_sum - 10
            node = ListNode(col_sum-10)
            cur_node.next = node

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        return head.next