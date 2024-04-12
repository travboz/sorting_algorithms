arr = [8, 16, 4, 12, 19, 3]


def insertion_sort(arr):
    n = len(arr)
    comparisons = 0

    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr, comparisons


# We do this so that this code only runs when you run `python insertion_sort.py`.
if __name__ == "__main__":
    print(insertion_sort(arr))
