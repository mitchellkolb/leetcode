

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
        
        
        
        # Step 1: Sort the input list so we can use the two-pointer approach.
        nums.sort()
        resultList = []
        n = len(nums)
        
        # Step 2: Iterate through each number, treating each as the first element (p1) of a triplet.
        for p1Index in range(n):
            # Skip duplicate values for p1 to avoid duplicate triplets.
            if p1Index > 0 and nums[p1Index] == nums[p1Index - 1]:
                continue
            
            # The target for the two-sum problem becomes the negative of the current p1.
            targetSum = -nums[p1Index]
            leftIndex = p1Index + 1
            rightIndex = n - 1
            
            # Step 3: Use a two-pointer approach on the subarray to the right of p1.
            while leftIndex < rightIndex:
                currentTwoSum = nums[leftIndex] + nums[rightIndex]
                
                if currentTwoSum < targetSum:
                    # Move the left pointer to increase the sum.
                    leftIndex += 1
                elif currentTwoSum > targetSum:
                    # Move the right pointer to decrease the sum.
                    rightIndex -= 1
                else:
                    # Found a valid triplet that sums to zero.
                    resultList.append([nums[p1Index], nums[leftIndex], nums[rightIndex]])
                    leftIndex += 1
                    rightIndex -= 1
                    
                    # Skip duplicate values for leftIndex.
                    while leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex - 1]:
                        leftIndex += 1
                    
                    # Skip duplicate values for rightIndex.
                    while leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex + 1]:
                        rightIndex -= 1
        
        return resultList

solution = Solution()
tests = [[-1,0,1,2,-1,-4], [0,1,1], [0,0,0]]
for test in tests:
    print(solution.threeSum(test))
