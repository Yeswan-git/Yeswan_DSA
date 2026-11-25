# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        def merge(l1 , l2):
            dummy = ListNode(0)
            res = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            
            while l1:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            
            while l2:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
            
            return res.next
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(merge(l1 , l2))
        
        return lists[0]