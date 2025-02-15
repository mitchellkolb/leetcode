




# 1290
# convert-binary-number-in-a-linked-list-to-integer

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

 

Constraints:

    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.


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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = ""
        ref = head

        while ref != None:
            temp = temp + str(ref.val)
            ref = ref.next

        return int(temp, 2)


if __name__ == "__main__":
    # Test cases:
    testInputs = [
        [1, 0, 1],
        [0]
    ]
    
    solution = Solution()
    
    for testCase in testInputs:
        print("\tOriginal List:", testCase)
        head = listToLinkedList(testCase)

        # HERE
        result = solution.getDecimalValue(head)

        #resultList = linkedListToList(result)
        print("\tOutput:", result)
        print("-" * 40)



