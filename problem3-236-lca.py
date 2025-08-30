# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# t(n) = o(n)
# s(n) = o(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == None:
            return root

        self.pathP = []
        self.pathQ = []

        self.dfs(root, p, q, [])

        for i in range(len(self.pathP)):

            if self.pathP[i] != self.pathQ[i]:
                break

        return self.pathP[i - 1]

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', path: List[TreeNode]) -> 'TreeNode':

        if root == None:
            return root

        # action
        path.append(root)

        if root == p:
            self.pathP = [i for i in path]
            self.pathP.append(root)

        if root == q:
            self.pathQ = [i for i in path]
            self.pathQ.append(root)

            # recurse
        self.dfs(root.left, p, q, path)
        self.dfs(root.right, p, q, path)

        # backtrack
        path.pop()