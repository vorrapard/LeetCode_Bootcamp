
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #step1 travese through tree to collect the numbers (BFS)
        numbers = []
        queue = deque([root])
        while queue:
            current_node = queue.popleft()
            numbers.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        #Step2 sort the numbers
        print(numbers)
        numbers.sort()
        print(numbers)

        return numbers[k-1]     #return the k-th number
