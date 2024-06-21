# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def initialize(self):
        self.level_nodes = []
        self.hash_maps = {}

    def level_order(self, root):
        count = 0
        queue = [(root, count)]

        while queue:
            new_root = queue.pop(0)
            self.level_nodes.append(new_root)

            if new_root[0].left or new_root[0].right:
                count = new_root[1]+1
            
            if new_root[0].left:
                queue.append((new_root[0].left, count))
            
            if new_root[0].right:
                queue.append((new_root[0].right, count))


    def post_order(self, root, leaf_nodes, checker, result):
        if not root or result:
            return checker, result, root
        
        left_checker, left_result, left_root = self.post_order(root.left, leaf_nodes, checker, result)
        right_checker, right_result, right_root = self.post_order(root.right, leaf_nodes, checker, result)

        if left_result:
            return left_checker, left_result, left_root
        if right_result:
            return right_checker, right_result, right_root

        child_checks = [x or y for x,y in zip(left_checker, right_checker)]

        root_checks = checker.copy()
        for i in range(len(leaf_nodes)):
            if leaf_nodes[i][0] == root:
                root_checks[i] = True

        final = [x or y for x,y in zip(child_checks, root_checks)]

        for each in final:
            if not each:
                result = False
                break
            else:
                result = True
        
        return final, result, root
            

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.initialize()
        self.level_order(root)

        leaf_nodes = []
        val = self.level_nodes[-1][1]
        for i in range(len(self.level_nodes)-1, -1, -1):
            if val == self.level_nodes[i][1]:
                leaf_nodes.append(self.level_nodes[i])
            else:
                break
        
        checker = [False]*len(leaf_nodes)
        final, result, root = self.post_order(root, leaf_nodes, checker, False)
        
        return root