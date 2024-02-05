
#  python -m unittest test.SortTest
from itog_lica import Sort
import unittest


class SortTest(unittest.TestCase):
    def test_counting_sort(self):
        nums = [3, 1, 4, 2, 1, 5]
        expected_result = [1, 1, 2, 3, 4, 5]

        result = Sort.counting_sort(nums)

        self.assertEqual(result, expected_result, f"Counting Sort is not working correctly: {result}")

    def test_selection_sort(self):
        nums = [4, 1, 3, 2, 5]
        expected_result = [1, 2, 3, 4, 5]

        result = Sort.selection_sort(nums)

        self.assertEqual(result, expected_result, f"Selection Sort is not working correctly: {result}")

    def test_heap_sort(self):
        nums = [4, 1, 3, 2, 5]
        expected_result = [1, 2, 3, 4, 5]

        result = Sort.heap_sort(nums)

        self.assertEqual(result, expected_result, f"Heap_sortis not working correctly: {result}")

    def test_bubble_sort(self):
        nums = [4, 1, 3, 2, 5]
        expected_result = [1, 2, 3, 4, 5]

        result = Sort.bubble_sort(nums)

        self.assertEqual(result, expected_result, f"Bubble Sort is not working correctly: {result}")

    def test_merge_sort(self):
        nums = [4, 1, 3, 2, 5]
        expected_result = [1, 2, 3, 4, 5]

        result = Sort.merge_sort(nums)

        self.assertEqual(result, expected_result, f"Merge_sort is not working correctly: {result}")

if __name__ == "__main__":
    unittest.main()

