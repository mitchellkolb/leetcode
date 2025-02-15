


# 876
# middle-of-the-linked-list

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

 

Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100


"""





# Leetcode doesn't provide enough boilerplate code to make their linked list code work and since I want to debug and/or visualize my solutions to solve them I want to use this boilerplate code to make it work.


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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # starting fast at head for when you want slow to get the second middle node on even lists
        # starting fast at head.next for when you want slow to get the first middle node on even lists
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow



if __name__ == "__main__":
    # Test cases:
    testInputs = [
        [1,2,3,4,5],
        [1,2,3,4,5,6]
    ]
    
    solution = Solution()
    
    for testCase in testInputs:
        print("\tOriginal List:", testCase)
        head = listToLinkedList(testCase)

        # HERE
        result = solution.middleNode(head)
        
        resultList = linkedListToList(result)
        print("\tOutput:", resultList)
        print("-" * 40)