





class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - convert all uppercase to lowercase
        - non-alphanumeric means???
            - whitespace
            - punctutation
            - other non english
        - reverse the string and see if they equal
        """
        cleanStr = ""

        for letter in s:
            if letter.isalnum():
                cleanStr += letter
        
        if cleanStr[::-1].lower() == cleanStr.lower():
            return True
        else:
            return False




solution = Solution()
tests = ["A man, a plan, a canal: Panama", "race a car", " "]
for test in tests:
    print(solution.isPalindrome(test))