class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_left = 0
        p_right = len(height)-1
        max_water = 0
        while (p_left != p_right):
            curr_water = min(height[p_left], height[p_right]) * (p_right-p_left)
            if (curr_water > max_water):
                max_water = curr_water
            if (height[p_left] > height[p_right]):
                p_right-=1
            else:
                p_left+=1
        return max_water
