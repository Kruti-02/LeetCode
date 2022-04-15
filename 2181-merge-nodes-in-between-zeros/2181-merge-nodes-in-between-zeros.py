# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        sum1=0
        dummy=ListNode(0)
        dum=dummy
        while(curr):
            if(curr.val==0):
                dum.next=ListNode(sum1)
                dum=dum.next
                sum1=0
            else:
                sum1+=curr.val
            curr=curr.next
        return dummy.next.next
        