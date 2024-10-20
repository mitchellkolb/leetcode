

# 271 encode-and-decode-strings
"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:

    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains only UTF-8 characters.

"""
from functools import reduce

class Solution:

    def encode(self, strs: list[str]) -> str:
        newCode = ""

        for word in strs:
            lengthWord = str(len(word))
            delimiter = "@"
            encodedWord = lengthWord + delimiter + word
            
            newCode = newCode + encodedWord
            
        return newCode
        
#Format of encode: (size of string)(delimiter)(string)


    def decode(self, s: str) -> list[str]:
        
        indice = 0
        seperatedStr = []

        

"""
Take the first bit of the string and get three parts the: Size, confirmation of @, rest of string
loop through the rest of the string size amount of times and make that its own item in the return list
repeat on the remaining rest of string with the first step
"""

solution = Solution()
tests = [["a", "bc", "d"], ["we","say",":","yes"], ["abc", "", "def"], ["ert", "sdf", ""], ["", "fdg", "cvb"], ["oneWord"], [""], []]

for test in tests:
    print(f"\n", test)
    resultInput = (solution.encode(test))
    print(resultInput)
    #print(solution.decode(resultInput))

