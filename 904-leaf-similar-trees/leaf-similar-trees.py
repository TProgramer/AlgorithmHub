# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Array to store leaf value of each trees
        leaf_values_1, leaf_values_2 = [], []

        # find leaf values of each trees with DFS
        def DFS(root, leaf_values):

            stack = [root]

            while stack:
                now_node = stack.pop()

                if now_node.left is None and now_node.right is None:
                    leaf_values.append(now_node.val)
                    continue
                
                if now_node.left is not None:
                    stack.append(now_node.left)
                if now_node.right is not None:
                    stack.append(now_node.right)
            
        DFS(root1, leaf_values_1)
        DFS(root2, leaf_values_2)

        return leaf_values_1 == leaf_values_2
                