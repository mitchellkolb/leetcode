

def quicksort(array: list[int]) -> list[int]:
    
    if len(array) < 2:
        return array
    else:
        # There are many ways of picking a "good" pivot point but since the array is unsorted my rendition will just be picking the first element
        pivot = array[0]
        left = [i for i in array[1:] if i <= pivot]
        right = [i for i in array[1:] if i > pivot] 
        
        return quicksort(left) + [pivot] + quicksort(right)



test_cases = [
    [],                   # Empty list
    [1],                  # Single element
    [5, 3, 8, 4, 2, 7, 6, 1],  # Random unsorted list
    [3, 3, 3, 3, 3],      # All elements are the same
    [10, 9, 8, 7, 6, 5],  # Already sorted in descending order
    [1, 2, 3, 4, 5],      # Already sorted in ascending order
    [5, 2, 8, 5, 3, 5],   # List with duplicates
    [6, 3, 8, 3, 2, 6, 1, 8], # List with mixed duplicates
    [5, -3, 8, -2, 1, -5, 3], # List with negative numbers
    [100, 50, 0, 50, 100],    # Large and duplicate values
]
for test in test_cases:
    print(quicksort(test))


"""
quicksort is a divide and conquer sorting algorithm that uses recursion to sort the input list. It does this with four things:

Base case: If the list is <= 1. This stops the recursion and also handles the empty list or single item list scenario.

Pick a pivot point which can be any item in the list

sort the list into two sections one that I'll call left which a list of every number that is less than the value of the pivot and then the other section called right which is a list of every number that is greater than the value of the pivot.

Then I call quick sort on left and right until the base case is reached.

As the call stack completes and the return statements arrive I then concatenate all the lists together and they should be sorted by doing this. Left list + pivot + Right List. Beause of the recursive nature of this algo all the left and right lists are sorted by the time they reach the inital recursive call.
"""

"""
This Time Complexity of Quicksort 
- Best Case O(n log n), when the pivot divides the array into balanced partitions.
- Worst Case O(n^2), when the pivot divides the array into highly unbalanced partitions (This could be a case when I've already sorted the array with a bad pivot choice)
- Average Case O(n log n)
"""