


"""
Backtracking is a brute force problem solving approach. It is not supposed to be used for optimization problems. It is used for when you want to find all possible solutions to a problem. It is an exhustive and brute force way of going through a set of input.


It does so by doing these couple of things:
1. Builds a solution incrementally
2. Abandons a solution as soon as it is determined it cannot lead to a valid answer based on the constraints.

This is some problems that would be useful for backtracking.
- Given a pair of parenteses generate all possible combinations
- Solving a maze/sudoku puzzle
- Generating permutations/combinations
- Solving the N-Queens Problem
- Subset Sum Problem


The Way to Make it Work:
- Start with an empty solution
- Explore the possibilities recursively and in every iteration adjust it slightly
- Backtrack when necessary by cutting the thread off to undo the last step and try another possibility


"""


def backtrack_subsets(start, path, nums, result):
    # Add the current subset to the result
    result.append(path[:])
    
    # Explore further subsets by including the next numbers
    for i in range(start, len(nums)):
        path.append(nums[i])  # Add current number to the path
        backtrack_subsets(i + 1, path, nums, result)  # Recursive call
        path.pop()  # Backtrack: Remove the last number

# Driver code
nums = [1, 2, 3]
result = []
backtrack_subsets(0, [], nums, result)
print(result)

"""
This is the output of the code above:
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

"""