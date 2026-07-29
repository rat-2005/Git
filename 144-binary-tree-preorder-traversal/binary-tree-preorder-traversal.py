# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array=[]
        def preorder(root,array):
            if root is None:
                return
            array.append(root.val)
            preorder(root.left,array)
            preorder(root.right,array)

        preorder(root,array)
        return array


        

        