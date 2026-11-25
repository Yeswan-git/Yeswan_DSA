# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None :
            return True  
        
        def reverse(head):
            curr = head
            prev = None

            while curr :
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        

        slow = fast = head

        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        
        new_head = reverse(slow.next)

        first , second = head , new_head

        while first and second :
            if first.val != second.val :
                return False
            first = first.next
            second = second.next
        
        slow.next = reverse(new_head)
        return True