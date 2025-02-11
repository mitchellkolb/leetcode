

# 15
# 3sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105


"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # check if list of lists converted into a set removes differently ordered lists. [[1,2,3],[1,3,2]]

        # I can just sort the list and then use an algo to find my hypothical solution in the list using my normal two sum solution. This would be my setup:
            # Sort the nums list
            # have one pointer go through the list call this p1
            # for every p1 item use my two sum algo on the rest of the list to the right of p1
            # Have to find out what to do with dups though
        pass

solution = Solution()
tests = [[-1,0,1,2,-1,-4], [0,1,1], [0,0,0]]
for test in tests:
    print(solution.threeSum(test))
