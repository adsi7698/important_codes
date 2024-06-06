# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def level_order(self, root):
        if root is None:
            return None

        queue = []

        queue.append(root)

        while len(queue) > 0:
            if queue[0]:
                self.level_values.append(queue[0].val)
            else:
                self.level_values.append(None)
            
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)


    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder_str.append(bin(root.val))
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            self.preorder_str.append(bin(root.val))
            self.preorder(root.left)
            self.preorder(root.right)

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        self.inorder_str = []
        self.preorder_str = []
        self.inorder(root)
        self.preorder(root)

        return ''.join(self.inorder_str) + '-' + ''.join(self.preorder_str)

    def initialize(self):
        self.preorder_index = 0

    def search(self, inorder_str, start, end, val):
        for i in range(start, end+1):
            if inorder_str[i] == val:
                return i

        return -1

    def get_data(self, inorder_str, preorder_str, start, end):
        if start > end or self.preorder_index >= len(preorder_str):
            return None

        node = TreeNode(preorder_str[self.preorder_index])
        self.preorder_index += 1

        if start == end:
            return node

        inorder_index = self.search(inorder_str, start, end, node.val)

        node.left = self.get_data(inorder_str, preorder_str, start, inorder_index-1)
        node.right = self.get_data(inorder_str, preorder_str, inorder_index+1, end)

        return node


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        inorder_str, preorder_str = data.split('-')
        inorder_str = inorder_str.split('0b')[1:]
        preorder_str = preorder_str.split('0b')[1:]
        
        inorder_str = [int(x, 2) for x in inorder_str]
        preorder_str = [int(x, 2) for x in preorder_str]
        self.initialize()
        node = self.get_data(inorder_str, preorder_str, 0, len(inorder_str))
        self.level_values = []
        self.level_order(node)

        count = len(self.level_values)
        for i in range(len(self.level_values)-1, -1, -1):
            if self.level_values[i] == None:
                count -= 1
            else:
                break

        return self.level_values[:count]


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans