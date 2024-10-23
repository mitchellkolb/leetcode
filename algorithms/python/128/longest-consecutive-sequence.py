

# 128 longest-consecutive-sequence

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        cleanSet = set(nums)
        result = 0

        for item in cleanSet:

            length = 0
            if item - 1 not in cleanSet: #Leftmost num in sequence
                while item + length in cleanSet:
                    length += 1
            result = max(length, result)

        return result


tests = [[], [0], [100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1]]

solution = Solution()
for test in tests:
    print(solution.longestConsecutive(test))


"""
Convert nums to a set to get rid of dups
I want to create a loop that goes through every item and checks to see if it is the leftmost number in the possible sequence.
I can do this by checking if n - 1 is in the set
    Once I'm at the leftmost number if at all I then do n + 1for as long as I can and increment a var
    Keep the higher var out of the two, the one I just counted vs the one that already exists
Once set loop is done then return result



This one took me a while to come up with a solution and I had to eventually watch a solution.
My inital way of trying to solve it was to use the fact that I an compare the length of nums to each number and if the distance between each number is greater than the length of nums then they must be two distinct sequences if at all. The issue I ran into was for numbers that belong to multiple sequences because they fit inbetween two possible sequences distance wise. The time complexity was more than O(n) which was a constraint. Obviously using the sorted() function wouldn't do it becuase it is O(nlogn).
"""