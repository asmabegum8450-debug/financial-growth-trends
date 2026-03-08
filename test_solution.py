import unittest
from solution import sorted_squares

class TestSortedSquares(unittest.TestCase):

    # Normal cases
    def test_case1(self):
        self.assertEqual(sorted_squares([-5,-2,0,3,10]), [0,4,9,25,100])

    def test_case2(self):
        self.assertEqual(sorted_squares([-8,-3,2,4,12]), [4,9,16,64,144])

    def test_case3(self):
        self.assertEqual(sorted_squares([-7,-1,2,3,11]), [1,4,9,49,121])

    # Edge cases
    def test_empty(self):
        self.assertEqual(sorted_squares([]), [])

    def test_single(self):
        self.assertEqual(sorted_squares([0]), [0])

    def test_all_negative(self):
        self.assertEqual(sorted_squares([-3,-2,-1]), [1,4,9])


if __name__ == "__main__":
    unittest.main()
