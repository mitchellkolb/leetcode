



# 138
# copy-list-with-random-pointer

"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

 

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

 

Constraints:

    0 <= n <= 1000
    -104 <= Node.val <= 104
    Node.random is null or is pointing to some node in the linked list.


"""

from typing import Optional, List

# Definition for singly-linked list.
class Node:
    def __init__(self, val: int, nextNode: 'Node' = None, randomNode: 'Node' = None):
        self.val = int(val)
        self.next = nextNode
        self.random = randomNode

    def __repr__(self):
        return f"Node({self.val})"


def listToLinkedList(dataList: List[List[Optional[int]]]) -> Optional[Node]:
    if not dataList:
        return None

    # First, create all nodes.
    nodes = [Node(item[0]) for item in dataList]

    # Then, link the nodes using the next pointers.
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Finally, assign random pointers based on the provided index.
    for i, item in enumerate(dataList):
        randomIndex = item[1]
        nodes[i].random = nodes[randomIndex] if randomIndex is not None else None

    return nodes[0]


def linkedListToList(head: Optional[Node]) -> List[List[Optional[int]]]:
    nodes = []
    nodeToIndex = {}
    currentNode = head

    # Traverse the list and build an index mapping.
    while currentNode:
        nodeToIndex[currentNode] = len(nodes)
        nodes.append(currentNode)
        currentNode = currentNode.next

    # Construct the output list: [node.val, randomIndex]
    outputList = []
    for node in nodes:
        randomIndex = nodeToIndex.get(node.random) if node.random is not None else None
        outputList.append([node.val, randomIndex])
    return outputList

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Create a mapping from old nodes to new nodes
        oldToNew = {}

        # First pass: create new nodes without linking next or random pointers
        currentNode = head
        while currentNode:
            oldToNew[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next

        # Second pass: assign next and random pointers
        currentNode = head
        while currentNode:
            newNode = oldToNew[currentNode]
            newNode.next = oldToNew.get(currentNode.next)
            newNode.random = oldToNew.get(currentNode.random)
            currentNode = currentNode.next

        # Return the head of the copied list
        return oldToNew[head]
        


if __name__ == "__main__":
    # Updated test cases: [node value, random pointer index (None if no random pointer)]
    testInputs = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]]
    ]
    
    solution = Solution()
    
    for testCase in testInputs:
        print("\tOriginal List:", testCase)
        head = listToLinkedList(testCase)

        # HERE: Call the copy function.
        result = solution.copyRandomList(head)

        resultList = linkedListToList(result)
        print("\tOutput:", resultList)
        print("-" * 40)
