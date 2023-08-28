# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        res = []        
        while root:
            if root.val != None: 
                if root.val == val:
                    return TreeNode(root.val, root.left, root.right)
                elif root.val > val:
                    root = root.left
                else:
                    root = root.right
            else:
                return root