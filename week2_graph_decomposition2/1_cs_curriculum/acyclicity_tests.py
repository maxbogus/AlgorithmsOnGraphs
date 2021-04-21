import unittest

from acyclicity import test


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(test([
            4, 4,
            1, 2,
            4, 1,
            2, 3,
            3, 1
        ]), 1)

    def test_sample_two(self):
        self.assertEqual(test([
            5, 7,
            1, 2,
            2, 3,
            1, 3,
            3, 4,
            1, 4,
            2, 5,
            3, 5
        ]), 0)


if __name__ == '__main__':
    unittest.main()
