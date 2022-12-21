# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_sym(left,right):
            
            # both left and right empty, which means both subtrees sym up to that point
            
            if not left and not right:
                return True
            
            # if one of left or right not present, return false
            if not left or not right:
                return False
            
            # if values of left and right, return false.
            if left.val != right.val:
                return False

            return is_sym(left.left, right.right) and is_sym(left.right,right.left)


        if not root:
            return True
        
        return is_sym(root.left,root.right)