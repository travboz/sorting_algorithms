import unittest
import random
from bubble_sort import bubble_sort


def generate_random_list(length, minimum, maximum):
    """
    Generates a random list of integers within the specified range.
    """
    return [random.randint(minimum, maximum) for _ in range(length)]


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_1(self):
        num_tests = 20
        for i in range(num_tests):
            unsorted = generate_random_list(i * 2, 1, 100)
            bubble_sorted, _comparisons = bubble_sort(unsorted)

            self.assertEqual(bubble_sorted, sorted(unsorted))

            print(f"Test {i+1} produced: {bubble_sorted}")


if __name__ == "__main__":
    unittest.main()
