# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafSequence(self, root):
        seq = []
        stack = [root]
        
        while len(stack) > 0:
            node = stack.pop()
            
            if not node.left and not node.right:
                seq.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return seq
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafSequence(root1) == self.getLeafSequence(root2)