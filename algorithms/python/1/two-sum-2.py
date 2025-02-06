



"""
- one use per element
- solution exists always. Cut out when found
- return the indices only

- One pass through the list
- every iteration subtract the current list number from the target. Put that value that we want to hoprfully see later in a dict as the key and the value is the indice it is at. 
check if in the dict the current list item exists in the dict if it does return that dict items value and the current indice.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        saved = {}
        result = []

        for indice, num in enumerate(nums):
            # check if current num is in dict
            if num in saved.keys():
                result.append(saved[num])
                result.append(indice)
                return result
            # add the flipped value to the dict to help out a future iteration
            else:
                desiredValue = target - num
                saved[desiredValue] = indice






solution = Solution()
tests = [[2, 7, 11, 15], 9, [3, 2, 4], 6, [3, 3], 6]
testsIterator = iter(tests)

for numberList, target in zip(testsIterator, testsIterator):
    print(solution.twoSum(numberList, target))