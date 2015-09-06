import random
import time

def padded_number(number, length):
    string_repr = str(number)
    for x in range(length - len(string_repr)):
        string_repr = ' ' + string_repr
    return string_repr

def AlreadyVisited(Exception):
    pass


def numeral_to_an(x, y):
    return chr(x + ord('a')), y + 1 


def an_to_numera(x, y):
    return ord(x) - ord(a), y - 1


def is_valid_point(x, y):
    return (
        0 <= x and x <=7 and
        0 <= y and y <=7
    )


def get_moves(x, y):
    moves = [
        (x + 1, y + 2), (x + 2, y + 1),
        (x + 2, y - 1), (x + 1, y - 2),
        (x - 1, y - 2), (x - 2, y - 1),
        (x - 2, y + 1), (x - 1, y + 2)
    ]
    return [move for move in moves if is_valid_point(*move)]

def random_point():
    return random.randint(0, 7), random.randint(0, 7)


class ChessBoard:
    def __init__(self):
        self.board = [[0 for row in range(8)] for column in range(8)]
        self.sequence = []
        self.step = 0
        self.board_size = 8

    def is_visited(self, x, y):
        return self.board[x][y] != 0

    def add_move(self, x, y):
        if self.is_visited(x, y):
            raise AlreadyVisited
        self.step += 1
        self.board[x][y] = self.step
        self.sequence.append((x, y))
        
    def get_last_move(self):
        return self.sequence[-1]

    def get_next_moves(self):
        start_point = self.get_last_move()
        moves = get_moves(*start_point)
        return self.filter_valid_moves(moves)

    def undo_last_move(self):
        x, y = self.sequence.pop()
        self.board[x][y] = 0
        self.step -= 1

    def filter_valid_moves(self, moves):
        return [move for move in moves if not self.is_visited(*move)]

    def orizontal_line(self):
        line = '   '
        for column in range(self.board_size):
            line += '+----'
        line += '+'
        return line

    def empty_line(self):
        line = '   '
        for column in range(self.board_size):
            line += '|    '
        line += '|'
        return line

    def numbered_line(self, number):
        line = '{} '.format(padded_number(number, 2))
        for column in range(self.board_size):
            line += '| {} '
        line += '|'
        return line

    def alfa_line(self):
        a = ord('a')
        letters = [chr(l) for l in range(a, a + self.board_size)]
        line = '   '
        for column in range(self.board_size):
            line += '   {} '
        return line.format(*letters)

    def __str__(self):
        string = ''
        for row in reversed(range(self.board_size)):
            values = [padded_number(self.board[x][row], 2) for x in range(self.board_size)]
            string += self.orizontal_line() + '\n'
            #string += self.empty_line() + '\n'
            string += self.numbered_line(row + 1).format(*values) + '\n'
            #string += self.empty_line() + '\n'
        string += self.orizontal_line() + '\n'
        string += self.alfa_line()
        return string


def solve_horse_problem(first_step=None):
    first_step = first_step or random_point()
    chessboard = ChessBoard()
    chessboard.add_move(*first_step)
    next_move = first_step or random_point()
    return solve(chessboard)


def solve(chessboard):
    #print chessboard
    #time.sleep(0.7)
    if chessboard.step == 8 * 8:
        return chessboard
    next_moves = chessboard.get_next_moves()
    for move in next_moves:
        chessboard.add_move(*move)
        solution = solve(chessboard)
        if solution:
            return solution
    chessboard.undo_last_move()
    return None


def main():
    chessboard = solve_horse_problem()
    print chessboard

if __name__=="__main__":
    main()