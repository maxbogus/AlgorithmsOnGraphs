import unittest
from dijkstra import test_function


class MyTestCase(unittest.TestCase):
    def test_first_sample(self):
        self.assertEqual(test_function([
            4, 4,
            1, 2, 1,
            4, 1, 2,
            2, 3, 2,
            1, 3, 5,
            1, 3
        ]), 3)


if __name__ == '__main__':
    unittest.main()
