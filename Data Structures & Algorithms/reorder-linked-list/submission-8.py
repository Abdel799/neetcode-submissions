# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start = slow.next
        prev = slow.next = None

        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        
        list1 = head
        list2 = prev

        while list2:
            temp1, temp2 = list1.next, list2.next

            list1.next = list2
            list2.next = temp1

            list1, list2 = temp1, temp2
        
        
        
