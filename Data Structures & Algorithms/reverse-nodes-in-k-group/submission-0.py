# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def findKth(current, k) -> Optional[ListNode]:
            for _ in range(k):
                if current == None:
                    break
                current = current.next
            
            return current
        
        dummy = ListNode(0, head)
        prev_group = dummy

        while True: 

            kth = findKth(prev_group, k)

            if kth != None:
                next_group = kth.next
            else:
                return dummy.next
            
            current = prev_group.next
            prev = next_group
            old_start = current

            while current != next_group:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            prev_group.next = prev
            prev_group = old_start


        