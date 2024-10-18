
#20. Valid Parentheses


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""




class Solution:
    def isValid(self, s: str) -> bool:
  
        stack = []

        closingSymbol = {")": "(", "]": "[", "}": "{"}

        for symbol in s:
            
            if symbol in closingSymbol.keys():
                # this means that the current symbol is a closing style one
                # I need to check the top of the stack to remove opening symbol
                if len(stack) == 0 or closingSymbol[symbol] != stack.pop():
                    return False
            else:
                stack.append(symbol)

        if len(stack) == 0:
            return True
        else:
            return False



solution = Solution()
tests = ["()", "()[]{}", "(]", "([])", "]", "["]
for test in tests:
    print(solution.isValid(test))
    

"""
What did I learn:

- mostly pythonic ways of doing stuff for example:
    - instead of my way of if symbol in closingSymbol.keys(): most other people do if symbol not in closingSymbol.   This just checks all the keys which both version do.
    - my final check of if the stack is empty to ensure all symbols have been used could've been done with this way of doing it apparently. return not stack

- While the time complexity of this is O(n) because I traverse the entire string the stack I used is slower in python. Apparently I should've used a collection.deque because the append and pop opertions of that is O(1) instead of the basic list which is O(n)

"""