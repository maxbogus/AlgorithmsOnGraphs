import unittest

from reachability import reach, test


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(test([
                             4, 4,
                             1, 2,
                             3, 2,
                             4, 3,
                             1, 4,
                             1, 4
                         ]), 1)


if __name__ == '__main__':
    unittest.main()
