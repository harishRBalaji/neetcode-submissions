# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
I - heads of 2 sorted linked lists
O - head of the merged sorted linked list
C - given
E - one node each, zero nodes in either of the sorted linked lists, zero nodes in both linked lists

Plan:
1. Create a new dummy node (result)
2. 2 temp pointers on both the heads
3. if temp1.val <= temp2.val:
    3.1 Create a new node with temp1.val and add to result node
    3.2 Else, do the same for the temp2
4. if temp1 is None:
    4.1. add temp2
    4.2 else, add temp1

5. return dummy.next
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode(-99, None)
        temp3 = dummy

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                node = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                node = ListNode(temp2.val)
                temp2 = temp2.next
            temp3.next = node
            temp3 = temp3.next
        
        if temp1:
            temp3.next = temp1
        if temp2:
            temp3.next = temp2
        
        return dummy.next
            





