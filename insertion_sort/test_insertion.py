import unittest
import random
from insertion_sort import insertion_sort


def generate_random_list(length, minimum, maximum):
    """
    Generates a random list of integers within the specified range.
    """
    return [random.randint(minimum, maximum) for _ in range(length)]


class TestInsertionSort(unittest.TestCase):

    def test_bubble_sort_1(self):
        num_tests = 20
        for i in range(num_tests):
            unsorted = generate_random_list(i * 2, 1, 100)
            insertion_sorted, _comparisons = insertion_sort(unsorted)

            self.assertEqual(insertion_sorted, sorted(unsorted))

            print(f"Test {i+1} produced: {insertion_sorted}")


if __name__ == "__main__":
    unittest.main()
