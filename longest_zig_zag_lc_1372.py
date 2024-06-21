# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zig_zag(self, root):
        if root:
            if root.left:
                root.val[0] = root.left.val[1] + 1
                if root.val[0] > self.result:
                    self.result = root.val[0]
            else:
                root.val[0] = 0

            if root.right:
                root.val[1] = root.right.val[0] + 1
                if root.val[1] > self.result:
                    self.result = root.val[1]
            else:
                root.val[1] = 0
        else:
            root.val = [0, 0]

        return root

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            root = self.zig_zag(root)

        return root 

    def inorder(self, root):
        if root:
            root.left = self.inorder(root.left)
            root.val = [-1, -1]
            root.right = self.inorder(root.right)

        return root
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        root = self.inorder(root)
        root = self.postorder(root)

        return self.result
        