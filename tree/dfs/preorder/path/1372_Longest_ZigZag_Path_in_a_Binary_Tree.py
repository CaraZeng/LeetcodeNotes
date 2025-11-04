"""
1372. Longest ZigZag Path in a Binary Tree
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or 
left).
If the current direction is right, move to the right child of 
the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the 
tree.
Zigzag length is defined as the number of nodes visited - 1. 
(A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: 
root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes 
(right -> left -> right).

Example 2:
Input: 
root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes 
(left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
 
Constraints:
The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""

# Key Note:
# 1. for every traverse, we either add 1 to length for another
# dir or start from this dir but set length to 1.
# 2. so actually we are counting every possible paths from 
# every possible nodes.
# 3. We keep track of prev_dir to decide where to move next.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, prev_dir, length):
        if not node:
            return
        self.longest = max(self.longest, length)
        if prev_dir == "L":
            self.traverse(node.right, "R", length + 1)
            self.traverse(node.left, "L", 1)
        else:
            self.traverse(node.left, "L", length + 1)
            self.traverse(node.right, "R", 1)
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.longest = 0
        self.traverse(root.left, "L", 1)
        self.traverse(root.right, "R", 1)
        return self.longest