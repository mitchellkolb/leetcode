


# 125 valid-palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Clean str of non-alphanumeric chars and capitals
        s = "".join(filter(str.isalnum, s))
        
        # Do initial check for strs that are < 1
        if len(s) <= 1:
            return True
        
        # len(str) is > 1 now we do the two pointers
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True       

"""
To solve this problem I'm going to use the two pointer approach.
This involves me having a variable at the start of the str and one at the end of the str.
During every iteration of the while loop:
    - Check this condition: Left and right are not past or on the same letter.
    - Adjust the left and right pointer if they are on non-alphanumeric chars
    - If they are verified chars then use .toLower() and compare
    - If Equal move onto next iteration
    - If Not Equal return false
Only go into the while loop if the input string is len() > 1
return true if its jst one letter and false if not
"""




solution = Solution()
tests = [
    "A man, a plan, a canal: Panama", 
    "race a car", 
    " ", 
    ":", 
    "12321", 
    "a", 
    "::aba#$"]
for test in tests:
    print(solution.isPalindrome(test))


"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.



"""