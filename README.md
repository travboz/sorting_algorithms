# Sorting Algorithms in Python
This repository contains my learning and testing of some of the fundamental sorting algorithms. The aim is to understand and rememeber the basic implementations of the algorithms.

### Bubble Sort
The key to this algorithm is thinking about the largest values being shifted or "bubbled" up to the right side (in ascending sorts). During each pass through the list, the largest 
unsorted element "bubbles up" to its correct position at the end of the list, while the smaller elements gradually "sink down" to the beginning.

**Time complexity**: For each element we could potentially walk it up the remaining length of the array. So, if we consider an array sorted in descending order of length `5`. 
We could be walking each consecutive element the length of the array. The first element would be walked:
```
[5, 4, 3, 2, 1] => [4, 3, 2, 1, 5] # has been walked four steps.
[4, 3, 2, 1, 5] => [3, 2, 1, 4, 5] # has been walked three steps.
[3, 2, 1, 4, 5] => [2, 1, 3, 4, 5] # has been walked two steps.
[2, 1, 3, 4, 5] => [1, 2, 3, 4, 5] # has been walked one step.
```
We perform this 'walking' for each element in the array. And so for `O(n)` elements, we traverse `O(n-1)` steps. This simplifies out to: `O(n^2).`
**Space complexity**: This is an in-place algorithm and so the space used remains constant, `O(1)`. 


### Insertion Sort




### How to use this repo
All of the algorithms are contained within their respective folders and will contain at least two files. 
I will use Bubble Sort as an example. 
Within See `sorting_algorithms/bubble_sort` there are two files. 
|File | Description| 
| -- | -- | 
| `bubble_sort.py` | Bubble sort algorithm implemented in Python. Contains a function which accepts an array and returns an, ascending order, sorted array. |
| `test_bubble.py` | Contains tests for the algorithm. |
