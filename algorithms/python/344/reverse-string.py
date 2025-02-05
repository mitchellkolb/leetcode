

# 344
# reverse-string

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.


"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) != 1:
            left = 0
            right = len(s) - 1
            
            while left <= right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp

                left += 1
                right -= 1
        
solution = Solution()
tests = [["h","e","l","l","o"], ["H","a","n","n","a","h"], ['a']]
for test in tests:
    solution.reverseString(test)