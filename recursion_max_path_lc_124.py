class Solution:
    def assignResult(self):
        self.result = 0
    
    def maxPaths(self, root):
        if root == None:
            return 0
        
        left_val = max(0, self.maxPaths(root.left))
        right_val = max(0, self.maxPaths(root.right))

        self.result = max(self.result, root.val + left_val + right_val)

        return root.val + max(left_val, right_val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        _ = self.maxPaths(root)
        return self.result