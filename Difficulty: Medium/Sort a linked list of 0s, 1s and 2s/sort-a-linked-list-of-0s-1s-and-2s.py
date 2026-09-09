'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        if not head : return head
        zeros = ones = twos = 0
        curr = head
        
        while curr :
            if curr.data == 0 :
                zeros += 1
            elif curr.data == 1 :
                ones += 1
            else:
                twos += 1
            curr = curr.next
        
        curr = head
        
        while zeros > 0:
            curr.data = 0
            curr = curr.next
            zeros -= 1
        while ones > 0 : 
            curr.data= 1
            curr = curr.next
            ones -= 1
        while twos > 0 :
            curr.data = 2
            curr = curr.next
            twos -= 1
        return head