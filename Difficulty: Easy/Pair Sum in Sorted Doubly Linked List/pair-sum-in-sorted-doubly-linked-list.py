# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        tail = head
        
        while tail.next :
            tail = tail.next
        
        l = head
        r = tail
        res = []
        
        while l is not None and r is not None and l is not r:
            s = l.data + r.data
            if s == target:
                res.append([l.data , r.data])
                l = l.next
                r = r.prev
            
            elif s < target:
                l = l.next
            
            else:
                r = r.prev
            
            if l is not None and r is not None and l.prev is r:
                break
        
        return res
            