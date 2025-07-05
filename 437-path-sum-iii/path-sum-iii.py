# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  

        def dfs(node, currSum):
            if not node:
                return 0
            currSum += node.val  
            count = prefix_sum[currSum - targetSum] 
            prefix_sum[currSum] += 1  
            count += dfs(node.left, currSum)  
            count += dfs(node.right, currSum) 
            prefix_sum[currSum] -= 1 
            return count
        return dfs(root, 0)
