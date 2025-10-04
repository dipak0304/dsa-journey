class Solution:
    def solveSudoku(self, board):
        self.row = [[False] * 9 for _ in range(9)]
        self.col = [[False] * 9 for _ in range(9)]
        self.box = [[False] * 9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    self.row[i][num] = self.col[j][num] = self.box[(i // 3) * 3 + j // 3][num] = True
        
        self.backtrack(board, 0, 0)
    
    def backtrack(self, board, r, c):
        if r == 9:
            return True
        if c == 9:
            return self.backtrack(board, r + 1, 0)
        if board[r][c] != '.':
            return self.backtrack(board, r, c + 1)
        
        for num in range(9):
            if not self.row[r][num] and not self.col[c][num] and not self.box[(r // 3) * 3 + c // 3][num]:
                board[r][c] = str(num + 1)
                self.row[r][num] = self.col[c][num] = self.box[(r // 3) * 3 + c // 3][num] = True
                
                if self.backtrack(board, r, c + 1):
                    return True
                
                board[r][c] = '.'
                self.row[r][num] = self.col[c][num] = self.box[(r // 3) * 3 + c // 3][num] = False
        
        return False