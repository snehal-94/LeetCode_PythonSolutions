Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

Solution_________________________________________________________________________

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## RC ##
        ## APPROACH : DFS ##
        ## Similar to leetcode 200. Number of Islands ##
        
        ## LOGIC ##
        # This problem is almost identical as the capture rule of the Go game, where one captures the opponent's stones by surrounding them. The difference is that in the Go game the borders of the board are considered to the walls that surround the stones, while in this problem a group of cells (i.e. region) is considered to be escaped (E) from the surrounding if it reaches any border.

		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(MxN) ##

        if len(board) < 2 or len(board[0]) < 2:
            return
        
        # making DFS calls only from borders.
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                self.dfs(board, i, len(board[0]) - 1)
                
        for j in range(1, len(board[0])):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[len(board) - 1][j] == 'O':
                self.dfs(board, len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':      # after DFS, its still "O", so it cannot escape, so merge with X
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                    
    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = 'E'           # can be escaped from border
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
