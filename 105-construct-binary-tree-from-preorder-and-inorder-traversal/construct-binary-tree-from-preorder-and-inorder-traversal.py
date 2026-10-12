# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return None

        
        root_value = preorder[0]

        root = TreeNode(root_value)


        root_index = inorder.index(root_value)

        
        root.left = self.buildTree(
            preorder[1:root_index + 1],
            inorder[:root_index]
        )

        
        root.right = self.buildTree(
            preorder[root_index + 1:],
            inorder[root_index + 1:]
        )

        return root