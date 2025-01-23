

# 22
# generate-parentheses

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8


"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Can't start with an open parentheses
        # Can't have more parentheses then 2n. Open < 2n
        # Only add a closing parentheses if closed < open
        # The func ends when open == closed == n

        res = [] #Holds the list of joined parentheses
        stack = [] #Holds the list of verified parentheses
        
        def backtrack(open, closed):
            # Base Case. Breaks the loop
            if open == closed == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
                
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res

solution = Solution()
tests = [3, 1]
for test in tests:
    print(solution.generateParenthesis(test))


