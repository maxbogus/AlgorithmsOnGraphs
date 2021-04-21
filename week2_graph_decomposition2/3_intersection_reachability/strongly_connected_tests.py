import unittest

from strongly_connected import test


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(test([
            4, 4,
            1, 2,
            4, 1,
            2, 3,
            3, 1
        ]), 2)

    def test_sample_two(self):
        self.assertEqual(test([
            5, 7,
            2, 1,
            3, 2,
            3, 1,
            4, 3,
            4, 1,
            5, 2,
            5, 3
        ]), 5)


if __name__ == '__main__':
    unittest.main()
