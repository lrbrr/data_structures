from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f'{self.left} <- {self.val} -> {self.right}'

class Solution:
    def recursor(self, root: Optional[TreeNode], result: List[int]):
        if root:
            self.recursor(root.left, result)
            result.append(root.val)
            self.recursor(root.right, result)
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.recursor(root, result)
        return result

example1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
#         1
#       /   \
#     2       3
#    /           
#   4   
print(Solution().inorderTraversal(example1)) # [4, 2, 1, 3]

example2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
#         1
#       /   \
#     2       3
#    /       / 
#   4       5   
print(Solution().inorderTraversal(example2)) # [4, 2, 1, 5, 3]