# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        dummy = Node(-1)
        dummy.next = head
        curr = dummy
        while curr.next :
            if curr.next.data == x:
                curr.next = curr.next.next
                if curr.next :
                    curr.next.prev = curr
            else:
                curr = curr.next
        
        return dummy.next