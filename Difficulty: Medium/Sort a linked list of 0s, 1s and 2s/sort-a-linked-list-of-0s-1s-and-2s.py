'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        l0 = Node(-1)
        l1 = Node(-1)
        l2 = Node(-1)
        zero = l0
        one = l1
        two = l2
        curr = head
        
        while curr:
            if curr.data == 0 :
                zero.next = curr
                zero = zero.next
            
            elif curr.data == 1 : 
                one.next = curr
                one = one.next
            
            else :
                two.next = curr
                two = two.next
            
            curr = curr.next
        
        zero.next = l1.next if l1.next else l2.next
        one.next = l2.next
        two.next = None
        return l0.next