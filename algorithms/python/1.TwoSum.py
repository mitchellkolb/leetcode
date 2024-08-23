
from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""





"""
My way to solve this solution_1:

1. Have two places one at the current indice moving left to right till end of list. The other which is one indice ahead and adds to it and then compares if that total == target
2. Need to check for bounds on last indice
3. If current indice is greater than target you can skip it

Cycing should be non-repetitive/shrinking as iterations go on

0 1
0 2
0 3

1 2
1 3

2 3

---------------
Accepted but slow
Negatives, tend to be rough
"""

#Attempt 1
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listSize = len(nums)
        #print(listSize)
        for i in range(len(nums)):
            currentIndice = i
            for j in range(len(nums)):
                #Move this to the next indice
                nextIndice = j + 1 + currentIndice

                #to check if j is in bounds
                if nextIndice > listSize - 1:
                    break
                
                if (nums[currentIndice] + nums[nextIndice] == target):
                    return(currentIndice, nextIndice)






"""
My way to solve this solution_2:

1. Using a dictionary because that has O(n) time for add and lookup
2. every indice I subtract from target and if the subtracted number is found in the dict I return the indice of the current value and the .value() of the one from the dict
3. else I add that current number as the key and its indice  as the value to the dict adn loop next

I can use enumerate to get value and indice every loop
---------------
Accepted and it was O(n) for space complex and time complex
"""
#Attempt 2
class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNum = {}

        for indice, value in enumerate(nums):
            print(value, indice)
            if (target - value) in dictNum:
                return [indice, dictNum[(target - value)]]
            else:
                dictNum[value] = indice




# Example usage:
nums = [2, 7, 11, 15]
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6

solution = Solution_1()
#result = solution.twoSum(nums, target)

solution = Solution_2()
result = solution.twoSum(nums, target)
print(result)
print("All Done")