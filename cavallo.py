

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
        (x+1, y+2), (x+2, y+1),
        (x+2, y-1), (x+1, y-2),
        (x-1, y-2), (x-2, y-1),
        (x-2, y+1), (x-1, y+2)
    ]
    return [move for move in moves if is_valid_point(*move)]


class ChessBoard:
    def __init__(self):
        self.board = [[0 for row in range(8)] for column in range(8)]
        self.sequence = []
        self.step = 0

    def is_visited(self, x, y):
        return self.board[x][y] != 0

    def add_move(self, x, y):
        if self.is_visited(x, y)
            raise AlreadyVisited
        self.step += 1
        self.board[x][y] = self.step
        self.sequence.append((x, y))

    def undo_last_move(self):
        x, y = self.sequence.pop()
        self.board[x][y] = 0
        self.step -= 1

    def filter_valid_moves(self, moves):
        return [move for move in moves if not self.is_visited(*move)]


def main():
    horse = Horse(2, 0)
    moves = horse.get_moves()
    an_moves = [numeral_to_an(*move) for move in moves]
    print an_moves


if __name__=="__main__":
    main()