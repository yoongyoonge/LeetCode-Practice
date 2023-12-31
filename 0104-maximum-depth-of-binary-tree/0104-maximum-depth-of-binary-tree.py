# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 재귀로 풀기
        def find_depth(root, depth):
            if not root: return depth
            return(max(find_depth(root.left, depth + 1), find_depth(root.right, depth + 1)))
        
        return (find_depth(root, 0))