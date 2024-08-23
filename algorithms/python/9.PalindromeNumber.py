
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Follow up: Could you solve it without converting the integer to a string?
"""




class Solution:
    def isPalindrome(self, x: int) -> bool:
        #print(x)
        try:
            rev = int(''.join(reversed(str(x))))
        except:
            rev = None
            
        if x == rev:
            return True
        else:
            return False



"""
This solution is O(n) for time because its two comparisons and its O(2n) for space becuase I create another number of the input 
"""

solution = Solution()
result = solution.isPalindrome(121)
result = solution.isPalindrome(-121)
result = solution.isPalindrome(10)