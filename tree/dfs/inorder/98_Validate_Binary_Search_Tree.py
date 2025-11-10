"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a 
valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys
strictly less than the node's key.
The right subtree of a node contains only nodes with 
keys strictly greater than the node's key.
Both the left and right subtrees must also be binary 
search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Key Note:
# 1. init a prev
# 2. for the mid part, first validate prev and root, then
# update root to prev
# 3. should return both left and right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isValidBST(root.left)
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        right = self.isValidBST(root.right)
        return left and right