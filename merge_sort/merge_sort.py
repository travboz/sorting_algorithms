def merge_sort(arr):
    n = len(arr)  # input array length

    if (
        n < 2
    ):  # less than 2 means we have either a single element or zero, so just return the array
        return arr

    # split the array in the left and right halves
    mid = n // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # recursively run merge_sort on the left and right halves
    merge_sort(leftHalf)
    merge_sort(rightHalf)

    # merge the left and right halves
    merge(arr, leftHalf, rightHalf)

    return arr


def merge(arr, leftHalf, rightHalf):
    leftSize = len(leftHalf)
    rightSize = len(rightHalf)

    i = 0  # traverses left half
    j = 0  # traverses right half
    k = 0  # traverses our output array

    # merging atomic arrays
    while i < leftSize and j < rightSize:
        if leftHalf[i] <= rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
        else:
            arr[k] = rightHalf[j]
            j += 1

        k += 1

    # adding the leftovers from left or right
    while i < leftSize:
        arr[k] = leftHalf[i]
        i += 1
        k += 1

    while j < rightSize:
        arr[k] = rightHalf[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [12, 5, 18, 29, 9, 26, 3, 22, 15, 7]
    print(merge_sort(arr))
