# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_val):
            if not node:
                return 0
            if node.val>=max_val:
                good=1
            else:
                good=0
            
            max_val=max(max_val,node.val)

            left_good=dfs(node.left,max_val)
            right_good=dfs(node.right,max_val)

            return good+left_good+right_good
        return dfs(root,root.val)