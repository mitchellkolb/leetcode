


# 1598  crawler-log-folder

# # Iterative soltuion
# class Solution:
#     def minOperations(self, logs: list[str]) -> int:
#         result = 0

#         for item in logs:
#             if item == "./":
#                 pass
#             elif item == "../":
#                 if result > 0:
#                     result = result - 1
#             else:
#                 # This is the change dir option
#                 result = result + 1

#         return result


# Stack based solution
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []

        for item in logs:
            if item == "./":
                pass
            elif item == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return len(stack)


solution = Solution()
tests = [["d1/","d2/","../","d21/","./"], ["d1/","d2/","./","d3/","../","d31/"], ["d1/","../","../","../"]]
for test in tests:
    print(solution.minOperations(test))


"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

    "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
    "./" : Remain in the same folder.
    "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

Example 2:

Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0

 

Constraints:

    1 <= logs.length <= 103
    2 <= logs[i].length <= 10
    logs[i] contains lowercase English letters, digits, '.', and '/'.
    logs[i] follows the format described in the statement.
    Folder names consist of lowercase English letters and digits.



"""