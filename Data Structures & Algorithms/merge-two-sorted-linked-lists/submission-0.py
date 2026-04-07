# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        curr3 = ListNode(-99)
        list3 = curr3

        while curr1 or curr2:
            if curr1 and curr2:
                node = None
                if curr1.val < curr2.val:
                    node = ListNode(curr1.val)
                    curr1 = curr1.next
                else:
                    node = ListNode(curr2.val)
                    curr2 = curr2.next
                curr3.next = node
            elif curr1:
                curr3.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr3 = curr3.next
        return list3.next