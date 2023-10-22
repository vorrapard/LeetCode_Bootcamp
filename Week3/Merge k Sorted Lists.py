# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) is 0:
            return None
        if len(lists) is 1:
            return lists[0]

        n = len(lists)
        output_head = ListNode()
        current = output_head
        minval = lists[0].val
        minindex = 0
        
        for i,item in enumerate(lists):
            if item is None:
                lists.pop(item)
            if item.val < minval:
                minval = item.val
                minindex = i



        
