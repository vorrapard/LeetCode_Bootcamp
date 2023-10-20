# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node = head
        while current_node != None:
            if current_node.val is "visited":
                return True
            current_node.val = "visited"
            current_node = current_node.next
        return False
