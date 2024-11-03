


# 2000 reverse-prefix-of-word


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []

        for spot, letter in enumerate(word):
            if letter == ch:
                stack.append(letter)
                # Begin reversing
                result = ''.join(stack)[::-1] + word[spot+1:]
                return result
            else:
                stack.append(letter)
        
        #The ch is not in the string. Return the string
        return word

solution = Solution()
tests = ["abcdefd", "d", "xyxzxe", "z", "abcd", "z"]
for item1, item2 in zip(tests[::2], tests[1::2]):
    print(solution.reversePrefix(item1, item2))

"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

 

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

 

Constraints:

    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.


"""