class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)

        count = [0] * (n+1)
        for a,b in edges:
            count[a-1] += 1
            count[b-1] += 1

        max_count = 0
        for i in range(len(count)):
            if count[i] > max_count:
                max_count = count[i]
                output = i+1
        return output
    

        
