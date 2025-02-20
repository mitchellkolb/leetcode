


# 74
# search-a-2d-matrix

"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104


"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # Determine the inner list that I want to BS on
        chosen_list = 0
        column_size = len(matrix[0])
        for i in range(len(matrix)):
            if matrix[i][column_size - 1] >= target:
                chosen_list = i
                break


        # Preform the BS on the chosen list
        left = 0
        right = len(matrix[chosen_list]) - 1
        middle = len(matrix[chosen_list]) // 2

        while left <= right:
            if matrix[chosen_list][middle] == target:
                return True
            elif matrix[chosen_list][middle] < target:
                left = middle + 1
            elif matrix[chosen_list][middle] > target:
                right = middle - 1
            else:
                print("Error in BS while loop")
            
            middle = (left + right) // 2
            

        return False



solution = Solution()
matrixs = [
    [[1], [3]], 
    [[1]], 
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    ]

targets = [2, 2, 30, 13]
for martix, target in zip(matrixs, targets):
    print(solution.searchMatrix(martix, target))