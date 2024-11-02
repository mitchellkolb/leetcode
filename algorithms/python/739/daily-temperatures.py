

# 739 daily-temperatures


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stackList = [] # List of lists where inner lists are pairs [temp, index]
        result = [0] * len(temperatures)

        for tempPlace, tempValue in enumerate(temperatures):
            while stackList and tempValue > stackList[-1][0]:
                stackValue, stackPlace = stackList.pop()

                resultValue = tempPlace - stackPlace
                result[stackPlace] = resultValue

            stackList.append([tempValue, tempPlace])

        return result 

"""

1. Looping through the temps and appending them to the stack if empty and doing #2 
if its not

2. for each item we compare it to the "top" of the stack and if its graeter then top we pop() it out and calculate it s result value and then put that in its place in the result list. Stop when stackList is empty or top is > current. Not equal too

3. once the array is looped go through and put 0's in for all the spots that were not accounted for.
"""



solution = Solution()
tests = [[73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90]]

for test in tests:
    print(solution.dailyTemperatures(test))


"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

 

Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100


"""