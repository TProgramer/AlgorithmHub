# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # if root is None, return empty array
        if root is None:
            return []

        # array for answer
        answer = []

        # find right side values with full depth of tree
        stack = [(root, 1)]
        while stack:

            now_node, depth = stack.pop()

            # update answer when arrive at new depth
            if depth > len(answer):
                print(now_node.val)
                answer.append(now_node.val)
            
            # add new left node first, to find right node first
            if now_node.left is not None:
                stack.append((now_node.left, depth + 1))
            if now_node.right is not None:
                stack.append((now_node.right, depth + 1))

        return answer