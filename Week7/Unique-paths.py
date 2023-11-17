class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = [[0 for column in range(n)] for row in range(m)]
        print(moves)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    moves[i][j] = 1
                else:
                    moves[i][j] = moves[i-1][j] + moves[i][j-1]

        print(moves)
        return moves[m-1][n-1]
