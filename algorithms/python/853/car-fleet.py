
# 853 car-fleet


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(cars)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
    
"""
fundamentally to solve this you compare the rightmost car with the next rightmost car and do a equation to figure out the time it takes for the cars to reach the target. If the 2nd right most car is faster which you can determine that by if the time it takes is less than the most right car. Then that must mean that they will at some point become a fleet before the target is reached.

time taken by car = (target - position / speed)

You then remove the car that is larger speed because they will go at the same slower speed

You sort the list becuase then when you start at the rightmost car you begin at the one that is closest to the target (AKA the end of the list) 

Sorting is done by quicksort at O(log n)
One pass through the list to combine to fleets is O(n)
That makes it O(nlogn) 

"""



solution = Solution()
tests = [
    [12, [10,8,0,5,3], [2,4,1,1,3]], 
    [10, [3], [3]],
    [100, [0,2,4], [4,2,1]]
    ]
for test in tests:
    print(solution.carFleet(*test))