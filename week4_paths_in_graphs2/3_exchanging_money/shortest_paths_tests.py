import unittest

from shortest_paths import test_function


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(test_function([6,7,
                                        1, 2, 10,
                                        2,3,5,
                                        1, 3, 100,
                                        3,5,7,
                                        5, 4, 10,
                                        4, 3, -18,
                                        6, 1, -1,
                                        1]), [0, 10, '-', '-', '-', '*'])

    def test_sample_two(self):
        self.assertEqual(test_function([5,4,
                                        1,2,1,
                                        4,1,2,
                                        2,3,2,
                                        3, 1, -5,
                                        4]), ['-', '-', '-', 0, '*'])


if __name__ == '__main__':
    unittest.main()
