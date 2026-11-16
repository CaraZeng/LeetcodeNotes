"""
Binary Tree Vertical Order Traversal
Medium
Topics
Company Tags
You are given the root node of a binary tree, return the vertical order traversal of its nodes' values.

For the vertical order traversal, list the nodes column by column starting from the leftmost column and moving to the right.

Within each column, the nodes should be listed in the order they appear from the top of the tree to the bottom.

If two nodes are located at the same row and column, the node that appears to the left should come before the other.

Example 1:



Input: root = [3,9,20,null,null,15,7]

Output: [[9],[3,15],[20],[7]]
Example 2:



Input: root = [3,9,8,4,0,1,7]

Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:



Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]

Output: [[4],[2,5],[1,10,9,6],[3],[11]]
Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""

# Key Note:
# 1. start from root and keep track of pos

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, pos = queue.popleft()
            if node:
                cols[pos].append(node.val)
                queue.append((node.left, pos - 1))
                queue.append((node.right, pos + 1))
        return [cols[x] for x in sorted(cols)]