


# 875
# koko-eating-bananas

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

 

Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109


"""
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # h has to be >= the length of piles that means 1 to the max item in piles is the range of numbers the output can be. Since the smallest that h can be is len(piles) that would mean I need koko to eat through every pile fully each hour with no carry over so the max would be required.
        # I can create an array of number ranging from 1 - max(piles) and do a binary search on it. For each number I test to see if koko eats through the whole pile or falls short after the alloted time frame and then adjust my bounds accordingly to find the minimum.
        # If my middle doesn't allow koko to finish that means koko doesn't eat enough in the time frame and we need to increase the output value so we would move left to middle + 1
        # If my middle finishes in the time frame that means we could have a solution but we need to know the minimum so we check if ... and if not adjust right to be middle - 1.

        result = max(piles)

        left = 1
        right = max(piles)

        while left <= right:
            middle = (left + right) // 2
            calculated_hours = 0

            for items in piles:
                calculated_hours += math.ceil(items / middle)
            
            if calculated_hours <= h:
                result = middle
                right = middle - 1
            elif calculated_hours > h:
                left = middle + 1
            else:
                print("ERROR")
            
        return result
         


solution = Solution()
piles = [[3,6,7,11], 
         [30,11,23,4,20], 
         [30,11,23,4,20]
]
hours = [8, 5, 6]
for pile, hour in zip(piles, hours):
    print(solution.minEatingSpeed(pile, hour))