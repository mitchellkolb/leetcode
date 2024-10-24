

# 1002 find-common-characters

from collections import defaultdict
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        mainDict = defaultdict(int)
        
        for letter in words[0]:
            mainDict[letter] += 1

        if len(words) >= 2:    
            tempDict = defaultdict(int)
            for word in words[1:]:
                tempDict.clear()
                for letter in word:
                    tempDict[letter] += 1

                #Comparing main and temp
                for key in list(mainDict.keys()):
                    if key in tempDict:
                        mainDict[key] = min(mainDict[key], tempDict[key])
                    else:
                        del mainDict[key]
                    


        result = []
        for key, value in mainDict.items():
            for i in range(0, value):
                result.append(key)

        return result
        

solution = Solution()
tests = [["bella","label","roller"], ["a"], ["cool","lock","cook"]]
for test in tests:
    print(solution.commonChars(test))



"""
- This solution is based on the idea that since I have to return the letters that exist in all str's. I just use the first string and make it into a dict where the letters are the key and the occurences are the values and compare all the letters in that to every other string which I make into a temp dict and remove key-value pairs from the main dict when they don't show up in the temp dict str in that iteration. I then just return whatever is left if anything at all.

I had to look up how to use do the comparison of the main dict in line 21 because you can't delete a key from a dict while looping through it so I had to make the keys into a list then loop through that which worked.
"""