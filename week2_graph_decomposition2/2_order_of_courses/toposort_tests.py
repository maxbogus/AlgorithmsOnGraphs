import unittest

from toposort import test


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(test([
            4, 3,
            1, 2,
            4, 1,
            3, 1
        ]), [4, 3, 1, 2])


if __name__ == '__main__':
    unittest.main()
