

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return res.values()




tests = [[""], ["a"], ["eat","tea","tan","ate","nat","bat"], ["a", "b", "c"]]

solution = Solution()
for test in tests:
    print(solution.groupAnagrams(test))