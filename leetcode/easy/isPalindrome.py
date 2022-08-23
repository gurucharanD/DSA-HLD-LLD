
# save head in a variable
# and keep going to the last node
# after reaching the last node start comparing it with the head node
# shift headpointer manually, node is shifted to the previous node by recursion

class Solution:
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.headPointer = head
        
        def helper(node):
        
            if node is None:
                return True
            
            if not helper(node.next):
                return False
            
            if self.headPointer.val != node.val:
                return False
            
            self.headPointer = self.headPointer.next
            return True
            
        return helper(head)
        