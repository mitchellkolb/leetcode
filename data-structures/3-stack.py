

class Stack:

    def __init__(self):
        self.stackList = []

    def push(self, val: int) -> None:
        self.stackList.append(val)

    def pop(self) -> int:
        return (self.stackList.pop(-1))

    def top(self) -> int:
        return self.stackList[-1]

"""
Stacks are a way of storing and handling data. While it is used in leetcode for sorting and searching problems its purpose is a way to store items in a first in last out format.
"""

stack = Stack()
nums = [1,2,3,4,5]
for num in nums:
    stack.push(num)
for i in range(len(nums)):
    print(stack.pop())
