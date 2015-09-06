import random
import time


def padded_number(number, length):
    string_repr = str(number)
    for x in range(length - len(string_repr)):
        string_repr = ' ' + string_repr
    return string_repr


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
    board_size = 8

    def __init__(self):
        self.board = [[0 for row in range(8)] for column in range(8)]
        self.friend_board = [[0 for row in range(8)] for column in range(8)]
        self.calculate_friend_board()
        self.sequence = []
        self.step = 0

    def calculate_friend_board(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.friend_board[x][y] = len(self.get_valid_moves(x, y))

    def add_friend_board(self, x, y):
        self.friend_board[x][y] = -1
        influenced = get_moves(x, y)
        for x, y in influenced:
            if self.friend_board[x][y] != -1:
                self.friend_board[x][y] -= 1

    def remove_friend_board(self, x, y):
        self.friend_board[x][y] = len(self.get_valid_moves(x, y))
        influenced = get_moves(x, y)
        for x, y in influenced:
            if self.friend_board[x][y] != -1:
                self.friend_board[x][y] += 1

    def is_visited(self, x, y):
        return self.board[x][y] != 0

    def add_move(self, x, y):
        if self.is_visited(x, y):
            raise AlreadyVisited
        self.step += 1
        self.board[x][y] = self.step
        self.sequence.append((x, y))
        self.add_friend_board(x, y)

    def get_last_move(self):
        return self.sequence[-1]

    def get_valid_moves(self, x, y):
        moves = get_moves(x, y)
        return self.filter_valid_moves(moves)

    def get_next_moves(self):
        if not self.worth_to_proceed():
            return []
        start_point = self.get_last_move()
        return self.get_valid_moves(*start_point)

    def worth_to_proceed(self):
        ones = 0
        for column in self.friend_board:
            for value in column:
                if value == 0:
                    return False
                if value == 1:
                    ones +=1
                    if ones == 2:
                        return False
        return True

    def undo_last_move(self):
        x, y = self.sequence.pop()
        self.board[x][y] = 0
        self.step -= 1
        self.remove_friend_board(x, y)

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

    def repr_board(self, board):
        string = ''
        for row in reversed(range(self.board_size)):
            values = [padded_number(board[x][row], 2) for x in range(self.board_size)]
            string += self.orizontal_line() + '\n'
            #string += self.empty_line() + '\n'
            string += self.numbered_line(row + 1).format(*values) + '\n'
            #string += self.empty_line() + '\n'
        string += self.orizontal_line() + '\n'
        string += self.alfa_line()
        return string

    def print_friends(self):
        print self.repr_board(self.friend_board)

    def __str__(self):
        return self.repr_board(self.board)

def solve_horse_problem(first_step=None):
    first_step = first_step or random_point()
    chessboard = ChessBoard()
    chessboard.add_move(*first_step)
    next_move = first_step or random_point()
    return solve(chessboard)


def solve(chessboard):
    #print chessboard
    #chessboard.print_friends()
    #time.sleep(0.2)
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