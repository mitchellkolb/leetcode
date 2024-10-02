class Solution:
    def scoreOfString(self, s: str) -> int:

        # loop through string letter by letter
        # at each letter check if there is a letter next in line
        # If yes convert current letter and next letter to ascii and then add the absolute difference of them
        # If no stop loop you have reached last letter and no equation is needed
        finalValue = 0
        strSize = 0
        while strSize <= (len(s)-2):
            # Setting iteration values
            mainLetter = ord(s[strSize])
            nextLetter = ord(s[strSize+1])

            # Calulating the added absolute difference
            temp = 0
            temp += (mainLetter - nextLetter)
            if temp <= -1:
                temp = (temp * -1)
            finalValue += temp

            # Loops to next iteration
            strSize += 1
        return finalValue


test = Solution()
print(test.scoreOfString("hello"))




"""
Time Complexity O(n) - length of the string
Space Compelxity O(1) - only need some value storing variables


3110: score-of-a-string
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

Constraints:

    2 <= s.length <= 100
    s consists only of lowercase English letters.


"""