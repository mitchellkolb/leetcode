
#########################################################################

#Find the number 32 in this list without iterating over the list one-by-one
def binarySearch(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low <= high:
        mid = (low + high) // 2  # Find the middle position
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            return binarySearch(arr, target, mid + 1, high)  # Search in the right half
        else:
            return binarySearch(arr, target, low, mid - 1)  # Search in the left half
    return -1  # Target not found

# Sorted list
listFindNumber = [2, 8, 4, 11, 14, 16, 19, 20, 25, 27, 32, 35, 40]
listFindNumber = sorted(listFindNumber)

# Perform the search
# result = binarySearch(listFindNumber, 32)

# if result != -1:
#     print(f"Number found at index: {result}")
# else:
#     print("Number not found.")

 #########################################################################


def binary_search(arr, target):
    """
    Performs binary search on a sorted array.

    Parameters:
    arr (list of int): The sorted array to search.
    target (int): The value to search for.

    Returns:
    int: The index of the target in the array if found, else -1.
    """
    low = 0 #start of array index
    high = len(arr) - 1 #end of the array index
    
    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        
        if guess == target:
            return middle
        elif guess < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 19
result = binary_search(arr, target)
#print(f"Index of {target} in the array is: {result}")
