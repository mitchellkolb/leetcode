

# 2807
# insert-greatest-common-divisors-in-linked-list

"""
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.

Example 2:

Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

 

Constraints:

    The number of nodes in the list is in the range [1, 5000].
    1 <= Node.val <= 1000


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
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = head.next

        while right:
            gcd_int = self.gcd(left.val, right.val)
            newNode = ListNode(gcd_int)
            left.next = newNode
            newNode.next = right

            left = right
            right = right.next

        return head

    def gcd(self, a: int, b: int) -> int:
        if (b == 0):
            return abs(a)
        else:
            return self.gcd(b, a % b)



if __name__ == "__main__":
    # Test cases:
    testInputs = [
        [7],
        [18,6,10,3]
    ]
    
    solution = Solution()
    
    for testCase in testInputs:
        print("\tOriginal List:", testCase)
        head = listToLinkedList(testCase)

        # HERE
        result = solution.insertGreatestCommonDivisors(head)

        resultList = linkedListToList(result)
        print("\tOutput:", resultList)
        print("-" * 40)
