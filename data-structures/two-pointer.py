


"""
- The two pointer technique is a general algorithmic method used to solve problems that involve searching or traversing elements of a data structure, usually arrays or linked lists. 
- It uses two pointers (indices or iterators) to efficiently traverse the data structure, reducing the time complexity compared to naive approaches.


Core Idea:
    Optimize traversal by narrowing the search space with two pointers instead of brute-forcing all possible combinations.


What you do: You maintain two pointers that move through the data structure in some way.


The movement can be:
    Towards each other (e.g., from the start and end of an array).
    In the same direction (e.g., for sliding window problems).
    From different starting points.


Common Use Cases:

    Searching in Sorted Arrays:
        Example: Find two numbers in a sorted array whose sum equals a target.
    Palindrome Checking:
        Use two pointers starting at the beginning and end of the string, moving inward.
    Merging Two Sorted Arrays:
        Use two pointers, one for each array, and compare elements as you merge them.
    Sliding Window Problems:
        E.g., Finding the longest substring with at most k distinct characters.


Time Complexity: Usually O(n)O(n), but can vary.






"""