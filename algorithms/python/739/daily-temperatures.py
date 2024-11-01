

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