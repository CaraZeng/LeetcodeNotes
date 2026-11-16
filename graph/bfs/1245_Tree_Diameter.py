"""
Tree Diameter
Medium
Topics
Company Tags
The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [aᵢ, bᵢ] indicates that there is an undirected edge between nodes aᵢ and bᵢ in the tree.

Return the diameter of the tree.


Example 1:



Input: edges = [[0,1],[0,2]]

Output: 2
Explanation: The longest path of the tree is the path 1 - 0 - 2.

Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]

Output: 4
Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


Constraints:

n == edges.length + 1
1 <= n <= 10⁴
0 <= aᵢ, bᵢ < n
aᵢ != bᵢ
"""

# Key Note:
# 1. 

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = [set() for i in range(len(edges) + 1)]
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)
        
        leaves = []
        for node, link in enumerate(graph):
            if len(link) == 1:
                leaves.append(node)
        
        layer = 0
        node_left = len(edges) + 1
        while node_left > 2:
            node_left -= len(leaves)
            next_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    next_leaves.append(neighbor)
            layer += 1
            leaves = next_leaves
        return layer * 2 + (0 if node_left == 1 else 1)