# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    final=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final=[]
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            final.append(root.val)
            traverse(root.right)

        traverse(root)
        return final

        

        