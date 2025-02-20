



# 704
# binary-search

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.


"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # bianry search is a three pointer searching algo that uses 3 pointers. You have a left, right, middle (right/2).
        # If middle is > target then right = middle and middle = right/2
        # If middle is < target then left = middle and then adjust middle
        # If middle == target return target

        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2 # floor division

        while left <= right:
            if nums[middle] == target:
                # return the index
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                print("error occured in while loop")
            middle = (left + right) // 2

        return -1

solution = Solution()
lists = [[-1,0,3,5,9,12], [-1,0,3,5,9,12], [4]]
targets = [9,2,3]

for list, target in zip(lists, targets):
    print(solution.search(list, target))