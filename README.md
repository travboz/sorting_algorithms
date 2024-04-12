# Sorting Algorithms in Python
This repository contains my learning and testing of some of the fundamental sorting algorithms. The aim is to understand the algorithms.

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

### Merge Sort
Merge sort is a divide and conquer algorithm. This means we **break the problem down** into parts and then break those parts down **into smaller problems**, and we continue to divide the problem into smaller and smaller problems until we have some **atomic problem** that we **can solve** (a base case). We then solve that subproblem (known as conquering) and follow that by **combining** all of the subproblems into the solution to our original problem. 

We apply this concept to merge sort by splitting the original array into two halves. We recurisvely perform merge sort of those two arrays until we have an array that is of size zero or one. The key is that an array of size one or zero is considered sorted - this becomes our base case. We now begin merging back all the arrays of size zero or one by combining them in order. We do this until we have an array of equal size to the original and we have now solved our original problem. 

![Merge sort algorithm diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/600px-Merge_sort_algorithm_diagram.svg.png "Merge sort algorithm diagram")
The above image shows the divide step (in Red), conquering step (in Gray), and finally the combining step (in Green). 


*Image attribution*
The image used in this README is "Merge sort algorithm diagram.svg" by [VineetKumar](https://www.doorstop.net/#/) at English Wikipedia. The original source of the image can be found on [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Merge_sort_algorithm_diagram.svg). This image is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

**Time complexity**: We use a recurrence to express the time complexity of merge sort. This recurrence relation is given by `T(n) = 2T(n/2) + O(n)`. 
We use the [Master theorem](https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture3.pdf) to solve this as our recurrence is of the form `T(n) = aT(n/b) + f(n)`. 
We can see that Merge Sort breaks the problem down into `a = 2` subproblems because we divide our larger array into **two** subarrays. Each array is of size `n/2` size where `b = 2`. In our combination/merge step, we perform `O(n)` work to merge each array at each combine step. 

For more information and analysis, please see:
[Solving Recurrences Example - Merge Sort](https://www.youtube.com/watch?v=gvfWeX8GCS8)

**Space complexity**: `O(n)` because we create temporary arrays `leftHalf` and `rightHalf` to divide the input array.



### How to use this repo
All of the algorithms are contained within their respective folders and will contain at least two files. 
I will use Bubble Sort as an example. 
Within See `sorting_algorithms/bubble_sort` there are two files. 
|File | Description| 
| -- | -- | 
| `bubble_sort.py` | Bubble sort algorithm implemented in Python. Contains a function which accepts an array and returns an, ascending order, sorted array. |
| `test_bubble.py` | Contains tests for the algorithm. |
