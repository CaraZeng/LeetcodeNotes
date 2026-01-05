"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end 
of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""

# Key Note:
# 1. fast moves n steps first the slow and fast moves together.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        while n:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next