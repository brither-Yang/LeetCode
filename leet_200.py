class Solution:
    def numIslands(self, grid):

        def dfs(grid, x, y):

            def inArea(x, y):
                return 0 <= x < m and 0 <= y < n

            grid[x][y] = 0
            for i in range(4):
                newX = x + direction[i][0]
                newY = y + direction[i][1]

                if inArea(newX, newY) and grid[newX][newY] is '1':
                    dfs(grid, newX, newY)
            return

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] is '1':
                    count += 1
                    dfs(grid, i, j)

        return count

ss = Solution()
print(ss.numIslands([[1, 1, 1, 1, 0],
                     [1, 1, 0, 1, 0],
                     [1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0]]))
