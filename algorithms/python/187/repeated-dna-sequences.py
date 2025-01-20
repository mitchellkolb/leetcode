


# 187
# repeated-dna-sequences
"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is either 'A', 'C', 'G', or 'T'.


"""




class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        # sliding window approach
        window = {}
        result = []
        left = 0
        right = 10

        if len(s) < 9:
            return result
        
        while right <= len(s):
            string = s[left:right]
            window[string] = window.get(string, 0) + 1
            left += 1
            right += 1

        for key, value in window.items():
            if value > 1:
                result.append(key)

        return result


solution = Solution()
tests = ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", "AAAAAAAAAAAAA", "A"]
for test in tests:
    print(solution.findRepeatedDnaSequences(test))