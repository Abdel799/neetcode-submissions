# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2

        if list2 == None:
            return list1

        result = ListNode()
        dummy = result

        head1 = list1
        head2 = list2

        while head1 != None and head2 != None:
            
            
            if head1.val <= head2.val:
                dummy.next = head1
                head1 = head1.next
            
            else:
                dummy.next = head2
                head2 = head2.next
            
            dummy = dummy.next
        
        if head1 != None:
            dummy.next = head1
        
        if head2 != None:
            dummy.next = head2
        
        return result.next
            
        
        