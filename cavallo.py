import random
import time


def padded_number(number, width):
    return str(number).rjust(width)


def cartesian_to_algebric_notation(x, y):
    return chr(x + ord('a')), y + 1 


def algebric_notation_to_cartesian(x, y):
    return ord(x) - ord('a'), y - 1


def is_valid_point(x, y, board_size):
    sup = board_size - 1
    return (
        0 <= x and x <= sup  and
        0 <= y and y <= sup
    )


def get_neighbours(x, y, board_size):
    moves = [
        (x + 1, y + 2), (x + 2, y + 1),
        (x + 2, y - 1), (x + 1, y - 2),
        (x - 1, y - 2), (x - 2, y - 1),
        (x - 2, y + 1), (x - 1, y + 2)
    ]
    return [move for move in moves if is_valid_point(move[0], move[1], board_size)]


def random_point(board_size):
    sup = board_size - 1
    return random.randint(0, sup), random.randint(0, sup)


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
        moves = get_neighbours(start_point[0], start_point[1], self.board_size)
        return self.filter_valid_moves(moves)

    def undo_last_move(self):
        x, y = self.sequence.pop()
        self.board[x][y] = 0
        self.step -= 1

    def filter_valid_moves(self, moves):
        return [move for move in moves if not self.is_visited(*move)]

    def __str__(self):
        renderer = BoardRenderer(self.board)
        return draw_ascii


class BoardRenderer:
    def __init__(self, board):
        self.board = board
        self.width = len(board)
        self.height = len(board[0])

    def line(self, pre, pattern, end):
        line = pre
        for column in range(self.width):
            line += pattern
        line += end
        return line

    def orizontal_line(self):
        return self.line('   ', '+----', '+')

    def empty_line(self):
        return self.line('   ', '|    ', '|')

    def numbered_line(self, number):
        return self.line('{} '.format(padded_number(number, 2)), '| {} ', '|')

    def alfa_line(self):
        a = ord('a')
        letters = [chr(l) for l in range(a, a + self.width)]
        line = self.line('   ', '   {} ', '')
        return line.format(*letters)

    def render(self):
        print self.draw_ascii()

    def draw_ascii(self):
        string = ''
        for row in reversed(range(self.height)):
            values = [padded_number(self.board[x][row], 2) for x in range(self.width)]
            string += self.orizontal_line() + '\n'
            #string += self.empty_line() + '\n'
            string += self.numbered_line(row + 1).format(*values) + '\n'
            #string += self.empty_line() + '\n'
        string += self.orizontal_line() + '\n'
        string += self.alfa_line()
        return string


def solve_horse_problem(first_step=None):
    first_step = first_step or random_point(8)
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