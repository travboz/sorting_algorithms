arr = [9, 18, 16, 5, 10, 8, 13, 3, 20, 1]

arr1 = [7, 3, 9, 2, 5]


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        # we do "n-i-1" to reduce the size of the window of values we're comparing with.
        # we do this because the end of the array is already sorted because the largest value would've already bubbled up.
        for j in range(
            0, n - i - 1
        ):  # if you change this to: "n-1" then it will double the number of comparisons
            # in this loop is where we're comparing elements
            comparisons += 1
            if (
                arr[j] > arr[j + 1]
            ):  # change the operator from `>` to `<` to reverse order of sort
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, comparisons


# print(bubble_sort(arr1))
