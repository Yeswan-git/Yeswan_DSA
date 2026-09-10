''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        def reverse(head):
            curr = head
            prev = None
            
            while curr :
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        head = reverse(head)
        carry = 1
        
        
        curr = head
        while curr :
            total = carry + curr.data
            if total <= 9 :
                curr.data = total
                carry = 0
            else:
                curr.data = 0
                carry = 1
            curr = curr.next
        
        head = reverse(head)
        
        if carry :
            new_node = Node(1)
            new_node.next = head
            head = new_node
            
        return head