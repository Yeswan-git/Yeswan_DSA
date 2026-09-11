''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        def helper(node):
            if node is None:
                return 1
            
            carry = helper(node.next)
            node.data = node.data + carry
            if node.data < 10 :
                return 0
            
            else: 
                node.data = 0
                return 1
        
        
        
        carry = helper(head)
        if carry :
            new_node = Node(1)
            new_node.next = head
            head = new_node
        
        return head