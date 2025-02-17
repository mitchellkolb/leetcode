


# 19
# remove-nth-node-from-end-of-list


"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

"""


from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def listToLinkedList(dataList: List[int]) -> Optional[ListNode]:
    dummyHead = ListNode(0)
    currentNode = dummyHead
    for num in dataList:
        newNode = ListNode(num)
        currentNode.next = newNode
        currentNode = newNode
    return dummyHead.next


def linkedListToList(head: Optional[ListNode]) -> List[int]:
    outputList = []
    currentNode = head
    while currentNode:
        outputList.append(currentNode.val)
        currentNode = currentNode.next
    return outputList


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Make two nodes, one that goes to end of list and other that is delayed from n iterations
        # When the first reaches the end I 
        
        # Edge case exception
        if head.next == None:
            return None
        
        # Move right n nodes forward 
        right = head
        while n != 0:
            right = right.next
            n -= 1

        # Make left start one behind head
        dummyHead = ListNode(0, head)
        left = dummyHead

        # Move to n-1 spot
        while right:
            right = right.next
            left = left.next

        # Deletion part
        newEnd = left.next.next
        left.next = newEnd

        # Return the list
        return dummyHead.next



if __name__ == "__main__":
    # Test cases:
    testInputs = [
        [1, 2, 3, 4, 5]
    ]
    testN = [
        5
    ]

    solution = Solution()
    
    for testList, nth in zip(testInputs, testN):
        print("\tOriginal List:", testList)
        head = listToLinkedList(testList)

        # HERE
        result = solution.removeNthFromEnd(head, nth)

        resultList = linkedListToList(result)
        print("\tOutput:", resultList)
        print("-" * 40)

