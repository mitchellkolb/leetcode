


# 2769
# find-the-maximum-achievable-number

"""
Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:

    Increase or decrease x by 1, and simultaneously increase or decrease num by 1.

Return the maximum possible value of x.

 

Example 1:

Input: num = 4, t = 1

Output: 6

Explanation:

Apply the following operation once to make the maximum achievable number equal to num:

    Decrease the maximum achievable number by 1, and increase num by 1.

Example 2:

Input: num = 3, t = 2

Output: 7

Explanation:

Apply the following operation twice to make the maximum achievable number equal to num:

    Decrease the maximum achievable number by 1, and increase num by 1.

 

Constraints:

    1 <= num, t <= 50


"""

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        calc = 2 * t
        calc = calc + num
        return calc

solution = Solution()
nums = [4, 3]
ts = [1, 2]

for num, t in zip(nums, ts):
    print(solution.theMaximumAchievableX(num, t))