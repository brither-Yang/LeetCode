class Solution:
    def exist(self, board, word):

        def backtrack(board, word, index, startx, starty):

            def inArea(x, y):
                return 0 <= x < m and 0 <= y < n

            if index == len(word)-1:
                return board[startx][starty] == word[index]

            if board[startx][starty] == word[index]:
                # 从 startx，starty 位置开始向四个方向寻找
                for i in range(4):
                    newX = startx + direction[i][0]
                    newY = starty + direction[i][1]
                    if inArea(newX, newY):
                        if visited[newX][newY] is False:
                            if backtrack(board, word, index+1, newX, newY):
                                return True

                visited[startx][starty] = False

            return False

        direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
        m = len(board)
        n = len(board[0])
        visited = [[False] * n] * m

        for i in range(m):
            for j in range(n):
                if backtrack(board, word, 0, i, j):
                    return True

        return False

ss = Solution()

print(ss.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCES"))