
#########################################################################

    
#Given a linkedList return the value of th emiddle node, if the length of the linked list is even, return the second middle value

#Example
#1 -> 2 -> 3
#return 2

#1 -> 2 -> 3 -> 4
#return 3

#1 -> 2 -> 3 -> 4 -> 5
#return 3

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def findMiddleNode(head):
    copyNode = head
    lenghtNum = 1
    while copyNode.next != None: #Finds the length of the linked list without destroying head
        lenghtNum += 1  
        copyNode = copyNode.next
    
    count = 0
    while count < (lenghtNum // 2): #Cycles through the linked list using floor division to get the right value
        head = head.next
        count += 1
        
    print(head.val)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

#findMiddleNode(head)