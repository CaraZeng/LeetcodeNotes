"""
437. Path Sum III
Given the root of a binary tree and an integer targetSum, return 
the number of paths where the sum of the values along the path 
equals targetSum.

The path does not need to start or end at the root or a leaf, but 
it must go downwards (i.e., traveling only from parent nodes to 
child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], 
targetSum = 22
Output: 3
 
Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""

# Key Note:
# 1. use a dict to record how many roads we have for this target sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, curr_sum, targetSum, prefix_count):
        if not node:
            return 0
        curr_sum += node.val
        count = prefix_count[curr_sum - targetSum]

        prefix_count[curr_sum] += 1
        count += self.traverse(node.left, curr_sum, targetSum, prefix_count)
        count += self.traverse(node.right, curr_sum, targetSum, prefix_count)
        prefix_count[curr_sum] -= 1
        return count
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        return self.traverse(root, 0, targetSum, prefix_count)