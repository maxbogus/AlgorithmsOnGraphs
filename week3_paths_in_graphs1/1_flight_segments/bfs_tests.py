import unittest

from bfs import test


class MyTestCase(unittest.TestCase):
    def test_first_sample(self):
        self.assertEqual(test([
            4, 4,
            1, 2,
            4, 1,
            2, 3,
            3, 1,
            2, 4
        ]), 2)

    def test_second_sample(self):
        self.assertEqual(test([
            5, 4,
            5, 2,
            1, 3,
            3, 4,
            1, 4,
            3, 5
        ]), -1)


if __name__ == '__main__':
    unittest.main()
