# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.count = -1
        self.inorder_list = []
        self.inorder(root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder_list.append(root.val)
            self.inorder(root.right)

    def next(self) -> int:
        self.count += 1
        return self.inorder_list[self.count]

    def hasNext(self) -> bool:
        if self.count+1 < len(self.inorder_list):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()