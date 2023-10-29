class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char is "(":
                stack.append(char)
            elif char is ")":
                if len(stack) == 0:
                    count += 1
                else:
                    if stack[-1] is "(":
                        stack.pop()

        return len(stack) + count         
