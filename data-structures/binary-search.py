


def binarySearch(nums: list[int], target: int) -> bool:
    left = 0
    mid = len(nums) // 2
    right = len(nums) - 1

    while left <= right:
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            #Adjust right
            right = mid - 1
        elif nums[mid] < target:
            #Adjust left
            left = mid + 1
        else:
            print("Error occured")
            
        #adjust left and right
        mid = (right + left) // 2

    return False





nums = [7, 17, 24, 31, 57, 62, 70, 81, 88, 99]
target = 10
print(binarySearch(nums, target))



"""
Binary search takes the middle part of a sorted array and the two ends and determines If == return True but if current middle value is < or > the target adjust the corresponding end to the other side of middle and then run it again till found or not found. 
"""

