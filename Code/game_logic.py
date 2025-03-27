import random

class gameplay:
    def __init__(self, size, mode= 'Simple game'):
        self.size = size
        self.mode = mode
        self.board = [['' for _ in range(size)] for _ in range(size)]
        self.current_turn = random.choice(['Blue', 'Red'])
        self.moves = []
        self.scores = {'Blue': 0, 'Red': 0}
        print(f"Game initialized: Size {size}, Mode {mode}")
        print(f"Start player: {self.current_turn}")
    
    def letterPlace(self, row, col, letter):
        if self.board[row][col] != '':
            return None, None

        self.board[row][col] = letter
        self.moves.append((row, col, letter, self.current_turn))

        sosList = self.checkForSos(row, col, letter)

        if sosList:
            self.scores[self.current_turn] += len(sosList)
            if self.mode == 'Simple':
                print(f"{self.current_turn} has won the game in Simple mode")
                return self.current_turn, sosList
            elif self.mode == 'General':
                if self.is_full():
                    winner = self.checkWinnerScore()
                    print(f"{winner} has won the game in general mode with a score of {self.scores[winner]}!")
                    return winner, sosList
            
        return None, sosList
            
    
        

    def switch_turn(self):
        self.current_turn = 'Red' if self.current_turn == 'Blue' else 'Blue'
        print(f"Turn is now {self.current_turn}")

    def sets_up_sos(self, row, col, letter):
        directions = [(-1,0), (1,0), (0, -1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
        for dr, dc in directions:
            if letter == 'S':
                if(0 <= row + 2*dr < self.size and 0 <= col + 2*dc < self.size and
                   self.board[row + dr][col + dc] == 'O' and
                   self.board[row +2*dr][col + 2*dc] == ''):
                    return True
                if(0 <= row + 2*dr < self.size and 0 <= col + 2*dc < self.size and
                   self.board[row + dr][col + dc] == '' and
                   self.board[row +2*dr][col + 2*dc] == 'S'):
                    return True
            elif letter == 'O':
                if (0 <= row + dr < self.size and 0 <= col + dc <self.size and
                     0 <= row - dr < self.size and 0 <= col - dc < self.size and
                     ((self.board[row + dr][col + dc] == 'S' and self.board[row - dr][col - dc] == '') or
                      self.board[row + dr][col + dc] == '' and self.board[row - dr][col - dc] == 'S')):
                    return True
        return False
    
    def complete_sos(self, row, col, letter):
        directions = [(-1,0), (1,0), (0, -1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
        for dr, dc in directions:
            if letter == 'S':
                if(0 <= row + 2*dr < self.size and 0 <= col + 2*dc < self.size and
                   self.board[row + dr][col + dc] == 'O' and
                   self.board[row +2*dr][col + 2*dc] == 'S'):
                    return True
            elif letter == 'O':
                if (0 <= row + dr < self.size and 0 <= col + dc <self.size and
                     0 <= row - dr < self.size and 0 <= col - dc < self.size and
                     ((self.board[row + dr][col + dc] == 'S' and self.board[row - dr][col - dc] == '') or
                      self.board[row + dr][col + dc] == '' and self.board[row - dr][col - dc] == 'S')):
                    return True
        return False
    
    def checkForSos(self, row, col, letter):
        if self.mode == 'Simple':
            return self.checkSimple(row, col, letter)
        elif self.mode == 'General':
            return self.checkGeneral(row, col, letter)
        else:
            sosList = []
        
    def checkSimple(self, row, col, letter):
        sosFound, coordinates = self.is_sos(row, col)
        if sosFound:
            return [coordinates]
        return []
    
    def checkGeneral(self, row, col, letter):
        sosList = []
        checkedPositions = set()
        directions = [(-1,0), (1,0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            sosFound, coordinates = self.is_sos_in_direction(row, col, dr, dc)
            if sosFound:
                    coordSet = frozenset(coordinates)
                    if coordSet not in checkedPositions:
                        sosList.append(coordinates)
                        checkedPositions.add(coordSet)
        return sosList if sosList else None
    
    def is_sos(self, row, col):
        directions = [(-1,0), (1,0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            sosFound, coordinates = self.is_sos_in_direction(row, col, dr, dc)
            if sosFound:
                return True, coordinates
        return False, None
    
    def is_sos_in_direction(self, row, col, dr, dc):
        try:
            if self.board[row][col] == 'O':
                if (0 <= row + dr < self.size and 0 <= col + dc < self.size and
                    0 <= row - dr < self.size and 0 <= col - dc < self.size):

                    if (self.board[row + dr][col + dc] == 'S' and
                        self.board[row - dr][col - dc] == 'S'):
                        return True, [(row - dr, col - dc), (row, col), (row + dr, col + dc)]
            elif self.board[row][col] == 'S':
                if (0 <= row + dr < self.size and 0 <= col + dc < self.size and
                    0 <= row + 2 * dr < self.size and 0 <= col + 2 * dc < self.size):
                    if (self.board[row + dr][col + dc] == 'O' and
                        self.board[row + 2 * dr][col + 2 * dc] == 'S'):
                        return True, [(row, col), (row + dr, col + dc), (row + 2 * dr, col + 2 * dc)]
        except IndexError:
            pass
        return False, None
    
    def is_full(self):
        full = all(self.board[r][c] != '' for r in range(self.size) for c in range(self.size))
        if full:
            print("The board is full.")
        return full
    
    def checkWinnerScore(self):
        if self.scores['Blue'] > self.scores['Red']:
            return 'Blue'
        elif self.scores['Red'] > self.scores['Blue']:
            return 'Red'
        else:
            print("The game is a draw.")
            return 'Draw'
