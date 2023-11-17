class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = list(text1)
        text2 = list(text2)
        m = len(text1)
        n = len(text2)
        longest = [[0 for column in range(n+1)] for row in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    longest[i][j] = longest[i-1][j-1] +1
                else:
                    longest[i][j] = max(longest[i-1][j], longest[i][j-1])
        print(longest)

        return longest[m][n]       
