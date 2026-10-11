# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head.next:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        slow = head
        fast = head

        while fast and fast.next:
            prev= slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return dummy.next    


            
        
        