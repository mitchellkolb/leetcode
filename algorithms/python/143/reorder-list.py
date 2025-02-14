


# 143
# reorder-list

"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

 

Constraints:

    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000


"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find middle of list
        once = head
        twice = head.next
        while twice and twice.next:
            once = once.next
            twice = twice.next.next
        
        # Reverse second list
        c2 = once.next
        n2 = None
        while c2:
            temp = c2.next
            c2.next = n2
            n2 = c2
            c2 = temp

        # Make end of first list .next go to null
        once.next = None

        # Weave in both lists
        first, second = head, n2
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2



tests = [[1,2,3,4], [1,2,3,4,5]]

solution = Solution()
for test in tests:
    print(solution.reorderList(test))

