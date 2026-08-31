# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_critical(prev , curr , nxt):
            return prev.val < curr.val > nxt.val or prev.val > curr.val < nxt.val
   
        first_crt = last_crt = -1
        prev , curr , nxt = head , head.next , head.next.next
        idx = 1
        min_dist = float("inf")
        while nxt:
            if is_critical(prev , curr , nxt):
                if first_crt == -1 :
                    first_crt = idx
                else:
                    min_dist = min(min_dist , idx - last_crt)
                
                last_crt = idx
            prev = curr
            curr = nxt
            nxt = nxt.next

            idx += 1
        
        if first_crt == -1 or first_crt == last_crt :
            return [-1 , -1]
        
        max_dist = last_crt - first_crt

        return [min_dist , max_dist]