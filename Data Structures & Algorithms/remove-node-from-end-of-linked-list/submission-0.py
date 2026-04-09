# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        removal_index = (size + 1) - n
        if removal_index == 1:
            return head.next
        prev = ListNode(-99, head) 
        curr = head
        while removal_index > 1:
            curr = curr.next
            prev = prev.next
            removal_index -= 1
        prev.next = curr.next
        curr.val = None
        curr.next = None
        return head
        