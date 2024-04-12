import unittest
import random
from merge_sort import merge_sort


def generate_random_list(length, minimum, maximum):
    """
    Generates a random list of integers within the specified range.
    """
    return [random.randint(minimum, maximum) for _ in range(length)]


class TestMergeSort(unittest.TestCase):

    def test_bubble_sort_1(self):
        num_tests = 20
        for i in range(num_tests):
            unsorted = generate_random_list(i * 2, 1, 100)
            merge_sorted = merge_sort(unsorted)

            self.assertEqual(merge_sorted, sorted(unsorted))

            print(f"Test {i+1} produced: {merge_sorted}")


if __name__ == "__main__":
    unittest.main()
