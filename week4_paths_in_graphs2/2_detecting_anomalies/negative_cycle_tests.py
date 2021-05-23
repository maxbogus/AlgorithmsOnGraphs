import unittest

from negative_cycle import test_function


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(test_function([4, 4,
                                        1, 2, -5,
                                        4, 1, 2,
                                        2, 3, 2,
                                        3, 1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
