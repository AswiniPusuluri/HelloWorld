import unittest
from game import player, computer, game


class MyTestCase(unittest.TestCase):
    def test_player(self):
        assert player() in ['R', 'P', 'S', 'L', 'V']

    def test_computer(self):
        assert computer() in ['R', 'P', 'S', 'L', 'V']

    def test_game(self):
        assert type(game()) is bool

if __name__ == '__main__':

 unittest.main()

