# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # slow goes to the mid pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second is the start of the second array
        second = slow.next
        prev = slow.next = None 

        # reverses second array
        # [0, 1, 2]
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev

        # merges list
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        
        
        