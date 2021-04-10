import unittest

from connected_components import test


class MyTestCase(unittest.TestCase):
    def test_input_one(self):
        self.assertEqual(test([
            4, 2,
            1, 2,
            3, 2
        ]), 2)


if __name__ == '__main__':
    unittest.main()
