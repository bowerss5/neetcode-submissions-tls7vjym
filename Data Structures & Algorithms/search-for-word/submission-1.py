class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set() 
        def backtrack(row, col, i):
            print(row, col, i)
            if i == len(word):
                return True
            if (row < 0 or col < 0 or row >= ROWS or
                col >= COLS or board[row][col] != word[i] or 
                (row, col) in path):
                return False
            path.add((row, col))
            result = (backtrack(row + 1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row - 1, col, i + 1) or
                    backtrack(row, col - 1, i + 1))
            path.remove((row, col)) 
            return result

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != word[0]:
                    continue
                if backtrack(row, col, 0):
                    return True
        return False
