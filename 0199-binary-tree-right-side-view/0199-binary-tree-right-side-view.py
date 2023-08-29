# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
 

        from collections import defaultdict

        l=defaultdict(int)
        def dfs(node,h):
            if node is None: return
                
            if h not in l:
                print(h) # 각 레벨에 맞는 값이 이미 있다면 입력하지않고 패스
                print(l)
                l[h]=node.val
            
            dfs(node.right, h+1) # 오른쪽 먼저 집어 넣고
            dfs(node.left, h+1)

        dfs(root, 0)

        print(l)

        return l.values()