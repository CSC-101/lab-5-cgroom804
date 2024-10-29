import data
import lab5
import unittest

from lab5 import time_add, is_descending, largest_between, furthest_from_origin


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        time1 = data.Time(5,31,26)
        time2 = data.Time(2, 15, 42)
        result = time_add(time1, time2)
        expected = data.Time(7, 47, 8)
        self.assertEqual(result, expected)

    def test_time_add2(self):
        time1 = data.Time(3,31,56)
        time2 = data.Time(6, 42, 18)
        result = time_add(time1, time2)
        expected = data.Time(10, 14, 14)
        self.assertEqual(result, expected)

    # Part 4
    def test_is_descending1(self):
        nums = [4,3,2,1]
        result = is_descending(nums)
        expected = True
        self.assertEqual(result, expected)

    def test_is_descending2(self):
        nums = [1,2,3,4]
        result = is_descending(nums)
        expected = False
        self.assertEqual(result, expected)

    # Part 5
    def test_largest_between1(self):
        lst = [4,6,2,5,7,2]
        result = largest_between(lst, -2, 7)
        expected = 4
        self.assertEqual(result, expected)

    def test_largest_between2(self):
        lst = [4, 6, 2, 5, 7, 2]
        result = largest_between(lst, 6, 8)
        expected = None
        self.assertEqual(result, expected)

    # Part 6
    def test_furthest_from_origin_1(self):
        points = [data.Point(3,4), data.Point(1,3), data.Point(2,2), data.Point(5,2)]
        result = furthest_from_origin(points)
        expected = 3
        self.assertEqual(result, expected)

    def test_furthest_from_origin_2(self):
        points = [data.Point(4, 4), data.Point(7, 3), data.Point(8, 5), data.Point(6, 4)]
        result = furthest_from_origin(points)
        expected = 2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
