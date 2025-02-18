
"""
A linked list is essentially a chain of nodes where each node holds some data along with a reference to the next node in line. This design makes it really easy to insert or remove elements anywhere in the list without having to shift the entire collection, unlike with arrays. However, because each element points to the next one, you can’t instantly jump to a specific spot—you have to start at the beginning and work your way through.

There are different types of linked lists, like singly linked lists where each node only points forward, and doubly linked lists that allow you to go both forwards and backwards. This flexibility makes linked lists a great choice when you’re dealing with a dynamic set of elements, such as in stacks, queues, or even more complex structures.

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
    def function(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head.val)
        print("ALRIGHT")



if __name__ == "__main__":
    # Test cases:
    testInputs = [
        [1],
        [1, 2, 3, 4, 5]
    ]
    
    solution = Solution()
    
    for testCase in testInputs:
        print("\tOriginal List:", testCase)
        head = listToLinkedList(testCase)

        # HERE
        result = solution.function(head)

        resultList = linkedListToList(result)
        print("\tOutput:", resultList)
        print("-" * 40)














"""
# Hints

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





"""