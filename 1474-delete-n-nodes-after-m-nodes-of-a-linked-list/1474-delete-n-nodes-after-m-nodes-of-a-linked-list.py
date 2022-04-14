# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        count =1
        
        curr = head
        while curr:
            if count == m:
                last_node=curr
                for i in range(n):
                    if curr.next:
                        curr = curr.next
                if curr:
                    last_node.next=curr.next
                    curr = curr.next
                    count =1
            else:
                curr = curr.next
                count+=1
        return head
        