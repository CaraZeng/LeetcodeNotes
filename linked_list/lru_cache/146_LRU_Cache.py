"""
146. LRU Cache
Solved
Medium
Topics
premium lock icon
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

# Key Note:
# 1. remember to handle linkedlist and dict at the same time.

class DLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.size = capacity
        self.head = DLinkedNode(-1, -1)
        self.tail = DLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        next = self.head.next
        self.head.next = node
        node.next = next
        node.prev = self.head
        next.prev = node
    def remove(self, node):
        next = node.next
        pre = node.prev
        pre.next = next
        next.prev = pre
    def get(self, key: int) -> int:
        if key not in self.cache:
            return - 1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        node = DLinkedNode(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.size:
            removed = self.tail.prev
            self.remove(removed)
            del self.cache[removed.key]