# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        r = [0]
        def find(node, a, b):
            if not node: 
                return
            r[0] = max(r[0], abs(node.val-a), abs(node.val-b))
            a = min(a, node.val)
            b = max(b, node.val)
            find(node.left, a, b)
            find(node.right, a, b)
        find(root, root.val, root.val)
        return r[0]