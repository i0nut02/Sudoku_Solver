import LRU_Cache


class Sudoku(object):

    def __init__(self, board = [[0 for _ in range(9)] for _ in range(9)]):
        self.board = board
        self.rows, self.cols, self.boxes = self.create_validation() 
        if self.rows == None or self.cols == None or self.boxes == None:
            self = None
            print("invalid board for Sudoku")

        self.missing_pos = self.find_missing_pos()


    def create_validation(self):
        rows = [set() for _ in range(len(self.board))]
        cols = [set() for _ in range(len(self.board[0]))]
        boxes = [set() for _ in range(len(self.board)**2 // 9)]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):

                num = self.board[i][j]
                box_indx = (i // 3) * 3 + j // 3

                if num == 0:
                    continue

                if num in rows[i]:
                    return None, None, None
                if num in cols[j]:
                    return None, None, None
                if num in boxes[box_indx]:
                    return None, None, None

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_indx].add(num)

        return rows, cols, boxes
    

    def is_valid(self, num, pos):
        i, j = pos

        if not (i < len(self.board) and j < len(self.board[0])):
            return False

        box_indx = (i // 3) * 3 + j // 3

        if num in self.rows[i]:
            return False

        if num in self.cols[j]:
            return False

        if num in self.boxes[box_indx]:
            return False
    
        return True


    def add(self, num, pos):
        i, j = pos

        if self.is_valid(num, pos):
            self.board[i][j] = num
            self.missing_pos.add((i, j))
            return True
        
        return False
    

    def remove(self, pos):
        i, j = pos
        if i < len(self.board) and j < len(self.board[0]):
            self.board[i][j] = 0
            self.missing_pos.remove(pos)


    def find_missing_pos(self):
        posionts_missing = LRU_Cache.lru_cache()
    
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    posionts_missing.add((i, j))
    
        return posionts_missing


    def solve(self):
        pos = self.missing_pos.get()

        if pos == None:
            return True
        
        i, j = pos 
        box_indx = (i // 3) * 3 + j // 3

        for num in range(1, 10):
            if self.is_valid(num, pos):

                self.board[i][j] = num
                self.rows[i].add(num)
                self.cols[j].add(num)
                self.boxes[box_indx].add(num)

                if self.solve():
                    return True
                else:
                    self.board[i][j] = 0
                    self.rows[i].remove(num)
                    self.cols[j].remove(num)
                    self.boxes[box_indx].remove(num)

        self.missing_pos.go_back()
        return False
    

    def __str__(self):
        out = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                out += "----------------------\n"
            for j in range(len(self.board)):
                if j % 3 == 0 and j != 0:
                    out += "| "
            
                out += str(self.board[i][j]) + " "
            out += "\n"
        return out

    
board = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
    ]

s = Sudoku(board)
s.solve()
a = Sudoku(s.board)
print(a)
        