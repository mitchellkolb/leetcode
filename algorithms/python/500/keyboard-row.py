

# 500 keyboard-row

"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []

Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

 

Constraints:

    1 <= words.length <= 20
    1 <= words[i].length <= 100
    words[i] consists of English letters (both lowercase and uppercase). 



"""

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        result = []
        listType = -1
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for word in words:            
            for i in range(0, 3):
                if word[0].lower() in keyboard[i]:
                    listType = i

            #Check if word len > 1 if no add to result
            if len(word) == 1:
                result.append(word)
                continue
            
            count = 0
            for letter in word:
                if letter.lower() in keyboard[listType]:
                    count += 1
            
            if count == len(word):
                result.append(word)

        return result



# clean the strings so that their all lower()



solution = Solution()
tests = [["a"], ["Hello","Alaska","Dad","Peace"], ["omk"], ["adsdf","sfd"]]
for test in tests:
    print(solution.findWords(test))



"""
Notes: 

- You can use <= or >= for sets to find any subsets so basically all the letters in the string exist in the set youre checking.
- I could've used all for the final condition to make it easier and not needing a loop.
"""