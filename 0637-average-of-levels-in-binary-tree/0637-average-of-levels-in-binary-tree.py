# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        from collections import deque

        q = deque([root])
        ans = []
        
        print(q)

        while q:
            qlen = len(q)
            print(qlen)
            row = 0

            for i in range(qlen):
                node = q.popleft()
                row += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(row/qlen)
        return ans