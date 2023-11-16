class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        
        minArrow = 1
        points = sorted(points)
        minRight = points[0][1]
        
        for balloon in points:
            if balloon[0] <= minRight:
                minRight = min(minRight, balloon[1])
            else:
                minArrow += 1
                minRight = balloon[1]
        
        return minArrow


        return 0
