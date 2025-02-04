


# 21
# merge-two-sorted-lists

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.



"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # For the printing of a single node
        return f"{self.val}"


def list_to_linked_list(values: List[int]) -> Optional[ListNode]:
    # Convert a Python list to a linked list
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    # Convert a linked list back to a Python list
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_previous = None
        l1_current = list1

        l2_previous = None
        l2_current = list2

        while l1_current and l2_current:
            print(l1_current, l2_current)

            l1_current.next
            l2_current.next

        return None


solution = Solution()
list1 = [[1,2,4], [], []]
list2 = [[1,3,4], [], [0]]

for item1, item2 in zip(list1, list2):
    print(solution.mergeTwoLists(item1, item2))
