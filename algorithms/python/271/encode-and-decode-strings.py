

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
        
        result = []
        left, right = 0, 0

        while left < len(s):

            #Getting the size before the @
            while s[right] != "@":
                right += 1
            
            #Add new string to list
            size = int(s[left:right])
            result.append(s[right + 1:right + 1 + size])

            #Adjust left/right for next iteration
            left = right + size + 1
            right = left + 1


        return result



        

"""
Take the first bit of the string and get three parts the: Size, confirmation of @, rest of string
loop through the rest of the string size amount of times and make that its own item in the return list
repeat on the remaining rest of string with the first step
"""

solution = Solution()
tests = [["we","say",":","yes","!@#$%^&*()"], ["a", "bc", "d"], ["we","say",":","yes"], ["abc", "", "def"], ["ert", "sdf", ""], ["", "fdg", "cvb"], ["oneWord"], [""], []]

for test in tests:
    print(f"\n", test)
    resultInput = (solution.encode(test))
    print(resultInput)
    print(solution.decode(resultInput))



"""
# This is an old crazy version I somehow got to pass all the cases but it is rough to read through

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
        
        result = []

        while s:

            #Assume that the string always starts at the start that I need it to
            lengthWord = ""
            stopper = True
            while stopper == True:
                if s[0] != "@":
                    lengthWord = lengthWord + s[0]
                    s = s[1:]
                else:
                    stopper = False
                
            lengthWord = int(lengthWord)
            
            delimiter = s[:1]
            s = s[1:]
            newStr = ""

            if lengthWord <= len(s):
                newStr = s[:lengthWord]
                s = s[lengthWord:]
                result.append(newStr)
            else:
                print("Error in while has occured")

        return result

"""