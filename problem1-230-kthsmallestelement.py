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


#time complexity - 0(n)
#space complexity - 0(h)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.result = -1
        self.count = 0
        self.dfs(root, k)
        return self.result

    def dfs(self, root: Optional[TreeNode], k: int) -> None:

        if root == None or self.result != -1:
            return

        self.dfs(root.left, k)

        self.count += 1

        if self.count == k:
            self.result = root.val
            return

        self.dfs(root.right, k)


#iterative way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#time complexity - 0(n)
#space complexity - 0(h)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root == None:
            return -1
        stack = []
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k - 1
            if k == 0:
                return root.val
            root = root.right