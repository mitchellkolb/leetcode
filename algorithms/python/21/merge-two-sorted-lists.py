


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

class ListNode:
    def __init__(self, value: int = 0, nextNode: Optional['ListNode'] = None):
        self.value = value
        self.nextNode = nextNode

    def __repr__(self):
        return f"ListNode({self.value})"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        holder = ListNode()
        result = holder
        
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next

        if list1:
            result.next = list1
        elif list2:
            result.next = list2

        return holder.next
        


# Helper function to convert a Python list to a linked list
def createLinkedList(inputList: List[int]) -> Optional[ListNode]:
    dummyNode = ListNode()
    currentNode = dummyNode
    for value in inputList:
        currentNode.nextNode = ListNode(value)
        currentNode = currentNode.nextNode
    return dummyNode.nextNode

# Helper function to convert a linked list back into a Python list
def linkedListToList(head: Optional[ListNode]) -> List[int]:
    resultList = []
    currentNode = head
    while currentNode is not None:
        resultList.append(currentNode.value)
        currentNode = currentNode.nextNode
    return resultList

if __name__ == '__main__':
    solution = Solution()
    list1 = [[1, 2, 4], [], []]
    list2 = [[1, 3, 4], [], [0]]

    for item1, item2 in zip(list1, list2):
        listOneHead = createLinkedList(item1)
        listTwoHead = createLinkedList(item2)
        mergedHead = solution.mergeTwoLists(listOneHead, listTwoHead)
        mergedList = linkedListToList(mergedHead)
        print(mergedList)

        """
        - pick the lesser head val in either list that is main. Larger value is other
        - have four variables setup for left and right value in both lists
        - if otherLeft is <= mainRight insert the node between mainLeft and mainRight
            - Adjust main left to be that new node 
            - move other left and right up one. 
            - next cycle
        - if otherLeft is > mainRight
            - move main left and right up one spot
            - next cycle
        """
        