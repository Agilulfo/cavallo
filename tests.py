import unittest
import random

from cavallo import get_neighbours, is_valid_point,\
    cartesian_to_algebric_notation, algebric_notation_to_cartesian,\
    padded_number, BoardRenderer

BOARD_SIZE = 8


def generate_board(width, height):
    max = width * height
    return [
        [random.randint(1, max) for row in range(height)]
        for column in range(width)
    ]


class UtilsTestCase(unittest.TestCase):

    def test_valid_point(self):
        self.assertTrue(is_valid_point(0, 0, BOARD_SIZE))
        self.assertTrue(is_valid_point(0, 7, BOARD_SIZE))
        self.assertTrue(is_valid_point(7, 0, BOARD_SIZE))
        self.assertTrue(is_valid_point(7, 7, BOARD_SIZE))
        self.assertTrue(is_valid_point(3, 2, BOARD_SIZE))

        self.assertFalse(is_valid_point(-2, 3, BOARD_SIZE))
        self.assertFalse(is_valid_point(2, -3, BOARD_SIZE))
        self.assertFalse(is_valid_point(8, 3, BOARD_SIZE))
        self.assertFalse(is_valid_point(3, 9, BOARD_SIZE))
        self.assertFalse(is_valid_point(-2, 9, BOARD_SIZE))

    def test_neighbours(self):
        board_size = 8
        neighbours = get_neighbours(0, 0, board_size)
        self.assertEqual(len(neighbours), 2)
        expected_neighbours = [(1, 2), (2, 1)]
        self.assertListEqual(neighbours, expected_neighbours)

    def test_coords_translation(self):
        self.assertEqual(cartesian_to_algebric_notation(0, 0), ('a', 1))
        self.assertEqual(cartesian_to_algebric_notation(3, 2), ('d', 3))
        self.assertEqual(algebric_notation_to_cartesian('a', 1), (0, 0))
        self.assertEqual(algebric_notation_to_cartesian('d', 3), (3, 2))

    def test_padded_number(self):
        self.assertEqual(padded_number(3, 3), '  3')
        self.assertEqual(padded_number(51, 2), '51')
        self.assertEqual(padded_number(123, 2), '123')

    def test_board_renderer(self):
        board = generate_board(8, 8)
        renderer = BoardRenderer(board)
        renderer.render()


if __name__=='__main__':
    unittest.main()
