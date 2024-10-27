

def selectionSort(nums: list[int], target: int) -> list[int]:
    
    if len(nums) <= 1:
        return nums
    print(nums)
    #print(len(nums))
    for left in range(0, len(nums) - 1):
        #print(f"\nnums[{left}]: {nums[left]}\t", end="")
        for right in range(left + 1, len(nums)):
            #print(right, end="  ")
            if nums[right] < nums[left]:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

    return nums


"""
Selection sort is a N^2 time complexity algo

It goes by you having a left check and a right check and you shift the right check all the way through the list until the end and on every iteration you compare the left and right value for whos is the minimum. If left < right move onto the next right item in the list is right < left then you switch the values of right and left so left now has the global minima after you cycle right through the entire list. After right reaches the end you adjust left by one and repeat the cycle again until you find the 2nd place minima and then by the time left is the 2nd to last item in the list the list is sorted becuase the least value is to the left of the current left value.
"""


#       0    1  2    3   4   5   6    7   8   9  10  11
nums = [58, 43, 66, 85, 100, 61, 87, 17, 89, 66, 96, 23]
target = 10
print(selectionSort(nums, target))
