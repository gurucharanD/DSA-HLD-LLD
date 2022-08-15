# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Using the intuition of reversing the entire linked list

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        def helper(prevNode,currNode,count):
            if currNode is None:
                return None
            
            tempCount = count
            temphead = currNode
            
            while temphead and tempCount:
                temphead = temphead.next
                tempCount -= 1
                
            if tempCount == 0:            
                k = count
                root = currNode
                while k != 0 and currNode:
                    nextNode = currNode.next
                    currNode.next = prevNode
                    prevNode = currNode
                    currNode = nextNode
                    k -= 1

                root.next = helper(None,currNode,count)

                return prevNode
            else:
                return currNode
        
        return helper(None,head,k)