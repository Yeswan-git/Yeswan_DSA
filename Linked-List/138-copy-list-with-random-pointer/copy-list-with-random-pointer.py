"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        hashmap = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next] if curr.next else None
            if curr.random:
                copy.random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]