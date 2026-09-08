''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        slow = fast = head
        length = 1
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast :
                slow = slow.next
                while slow != fast:
                    length += 1
                    slow = slow.next
                return length
        return 0