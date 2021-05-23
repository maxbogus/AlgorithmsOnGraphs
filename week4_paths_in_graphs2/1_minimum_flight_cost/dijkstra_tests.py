import unittest
from dijkstra import test_function


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(test_function([
            4, 4,
            1, 2, 1,
            4, 1, 2,
            2, 3, 2,
            1, 3, 5,
            1, 3
        ]), 3)

    def test_sample_two(self):
        self.assertEqual(test_function([
            5, 9,
            1, 2, 4,
            1, 3, 2,
            2, 3, 2,
            3, 2, 1,
            2, 4, 2,
            3, 5, 4,
            5, 4, 1,
            2, 5, 3,
            3, 4, 4,
            1, 5
        ]), 6)


if __name__ == '__main__':
    unittest.main()
