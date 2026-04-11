# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        prev = None

        # find middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # store second half values in stack
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next

        # cut off first half
        if prev:
            prev.next = None

        # insert nodes from stack after each first-half node
        curr = head
        last = None
        while curr and stack:
            nxt = curr.next
            node = ListNode(stack.pop(), nxt)
            curr.next = node
            last = node
            curr = nxt

        # if one value is left, append it at the end
        if stack and last:
            last.next = ListNode(stack.pop())
