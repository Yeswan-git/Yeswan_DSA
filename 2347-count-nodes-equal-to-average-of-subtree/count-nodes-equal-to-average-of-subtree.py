# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matches = [0]

        def post_order(node):
            if not node :
                return 0 , 0
            
            left_sum , left_count = post_order(node.left)
            right_sum , right_count = post_order(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                matches[0] += 1
            
            return total_sum , total_count
        
        post_order(root)
        return matches[0]