# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummy_head = ListNode()
        current_head = dummy_head
        
        while(list1 and list2):
            if list1.val > list2.val:
                current_head.next = list2
                list2 = list2.next
            else:
                current_head.next = list1
                list1 = list1.next
            current_head = current_head.next
        
        if list1:
            current_head.next = list1
        if list2:
            current_head.next = list2
        
        return dummy_head.next