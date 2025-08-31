# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#time complexity - 0(n)
#space complexity - 0(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []
        self.dfs(root)
        return self.result[k - 1]

    def dfs(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return

        self.dfs(root.left)
        self.result.append(root.val)
        self.dfs(root.right)