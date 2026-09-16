# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        curr = headRef
        
        while curr and curr.next:
            new_distinct = curr.next
            
            while new_distinct and new_distinct.data == curr.data :
                new_distinct = new_distinct.next
            
            curr.next = new_distinct
            
            curr = curr.next
        
        return headRef