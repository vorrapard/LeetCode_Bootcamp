# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        output = []
        current_level = []
        next_level = deque()
        myqueue = deque([root])

        while myqueue:
            current = myqueue.popleft()
            current_level.append(current.val)
            if current.left is not None:
                next_level.append(current.left)
            if current.right is not None:
                next_level.append(current.right)
            
            if not myqueue:
                if current_level != []:
                    output.append(current_level)
                    current_level = []
                myqueue = next_level
                next_level = deque()


        return output




        
