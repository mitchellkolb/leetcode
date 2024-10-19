

# 347 top-k-frequent-elements
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        store = {}
        result = []

        for ints in nums:
            if ints in store:       #Checking if the number exists in dict
                store[ints] += 1
            else:
                store[ints] = 1     #Adding the number occurence of the num otherwise

        for i in range(0,k):
            willAppend = max(store, key=store.get) #Gets the key in the dict that has the highest .value
            result.append(willAppend) #Adds that key value to the list
            store.pop(willAppend) #Removes that key-value pair from dict

        return(result)


solution = Solution()
tests = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([1, 2, 3], 3)]
for listA, intB in tests:
    print(solution.topKFrequent(listA, intB))



"""
I loop through every item in the nums array and at each item I do this
    - Have a dict to store the value as the key (unqiue) and the number of occurences as the value
        - If its the first time I am seeing the number I put it as a key and make the value 1
        - If NOT the first time I increment the value at that key by 1
I then do a loop with K iterations and at each iteration I do this
    - Have a result list to return at the end.
    - Every iteration I find the max() .value in the dict
        - then .append the .key value of the current max() to the result list
        - then I remove the key-value pair from the dict and move onto next iteration
Return the result list


Worst Case
O(n) dict insert through nums {1: 1, 2: 1, 3: 1} 
O(1) for dict lookup and other constants for append and conditions, which get droped for overal time complex
"""