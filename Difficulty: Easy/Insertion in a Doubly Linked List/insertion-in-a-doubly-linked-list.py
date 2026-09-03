''' Structure of Doubly Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        curr = head
        for i in range(p):
            curr = curr.next
        
        new_node = Node(x)
        new_node.next = curr.next
        if curr.next :
            curr.next.prev = new_node
        
        curr.next = new_node
        new_node.prev = curr
        
        return head