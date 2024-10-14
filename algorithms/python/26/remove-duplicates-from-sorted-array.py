
# remove-duplicates-from-sorted-array

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Constraints:

    1 <= nums.length <= 3 * 104      <------------- This means we dont have to worry about empty array
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]: #This is the first time we are seeing a new number and we need to switch it
                nums[left] = nums[right]
                left += 1
        return left


solution = Solution()
tests = [[1,1,2], [0,0,1,1,1,2,2,3,3,4], [1,2,3,4,5]]

for test in tests:
    print(solution.removeDuplicates(test))



"""
My solution uses two pointers where the left keeps track of the last position to switch with the int when a new one if came across when the right pointer moves along the list.

What did I learn in doing this.
    -   range() can have a starting point with mine starting at 1
 

"""