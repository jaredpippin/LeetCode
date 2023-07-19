# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): #making another function bc we want return of [Bool,height]
            #base case
            if not root:
                return [True,0]
            left,right = dfs(root.left), dfs(root.right) #get left and right nodes
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1) #checking for bool of L & R subtrees/nodes
            
            return [balanced, 1+max(left[1],right[1])] #bool,height returned
        
        return dfs(root)[0] #return only the first return val, which is the balanced bool
            