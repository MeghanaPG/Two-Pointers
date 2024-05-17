class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time complexity: Number of cells = O(9^2)
        # Hashmap to detect the duplicate; where key is going to be the col number and values is going to be set 
        # Note: we don't have to check if 1-9 is the digit present in the board because, it is given that the board contains only 1-9 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) 
        # key = (r/3,c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                
                if(board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                    # otherwise we will add the values to the respective rows and cols 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True