# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



'''
Better way to solve this problem in one iteration would be to -
iterate as you go, add each level's values together, meanwhile changing that node's value to
negative of their parent's children. This way, first it will be negation of sum of its parents 
children and then sum of all nodes present in that level.
'''



class Solution:
    def level_order_updates(self, root):
        queue = []
        depth = 0
        queue.append([root, root, depth])
        total = 0

        while queue:
            cur = queue.pop(0)
            if depth == cur[2]:
                temp = 0
                if cur[1].left:
                    temp += cur[1].left.val
                if cur[1].right:
                    temp += cur[1].right.val

                total += temp

                if cur[0] != cur[1]:
                    temp = 0
                    if cur[0].left:
                        temp += cur[0].left.val
                    if cur[0].right:
                        temp += cur[0].right.val
                    self.node_map[cur[1]] = temp
            else:
                self.hash_map[depth] = total
                depth += 1

                total = 0
                if cur[1].left:
                    total += cur[1].left.val
                if cur[1].right:
                    total += cur[1].right.val

                temp = 0
                if cur[0].left:
                    temp += cur[0].left.val
                if cur[0].right:
                    temp += cur[0].right.val
                self.node_map[cur[1]] = temp

            if cur[1].left:
                queue.append([cur[1], cur[1].left, cur[2]+1])
            if cur[1].right:
                queue.append([cur[1], cur[1].right, cur[2]+1])

        self.hash_map[depth] = total

        return root

    def level_order(self, root):
        queue = []
        depth = 0
        queue.append([root, depth])

        while queue:
            cur = queue.pop(0)

            if cur[1] < 2:
                cur[0].val = 0
            else:
                cur[0].val = self.hash_map[cur[1]-1] - self.node_map[cur[0]]

            if cur[0].left:
                queue.append([cur[0].left, cur[1]+1])
            if cur[0].right:
                queue.append([cur[0].right, cur[1]+1])

        return root
    

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.hash_map = {}
        self.node_map = {}

        root = self.level_order_updates(root)
        root = self.level_order(root)

        return root