import unittest

from toposort import test


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(test([
            4, 3,
            1, 2,
            4, 1,
            3, 1
        ]), [4, 3, 1, 2])

    def test_sample_two(self):
        self.assertEqual(test([
            4, 1,
            3, 1
        ]), [2, 3, 1, 4])

    def test_sample_three(self):
        self.assertEqual(test([
            5, 7,
            2, 1,
            3, 2,
            3, 1,
            4, 3,
            4, 1,
            5, 2,
            5, 3
        ]), [5, 4, 3, 2, 1])

    if __name__ == '__main__':
        unittest.main()
