# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = {}
        currentNode = head
        i = 0

        while currentNode != None:

            if currentNode not in seen:
                seen[currentNode] = i
            
            else:
                return True
            
            i+=1
            currentNode = currentNode.next
        
        return False
        