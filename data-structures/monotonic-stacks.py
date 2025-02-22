

"""
Monotonic stacks are a cool twist on the regular stack data structure. Instead of just adding elements in a last-in-first-out way, a monotonic stack keeps its elements in a sorted order—either strictly increasing or decreasing. When you push a new element, you pop off any items that would break that order. This is super handy for problems like finding the next greater or smaller element in an array.

Even with these extra checks during push operations, the average time for push, pop, and peek remains O(1). You can think of it as a regular stack with a built-in way to keep things sorted on the fly. Here's a quick example of a basic stack (using camelCase for variable names) that you could adapt into a monotonic stack by tweaking the push method:

"""

class Stack:
    def __init__(self):
        self.stackList = []

    def push(self, val: int) -> None:
        self.stackList.append(val)

    def pop(self) -> int:
        return self.stackList.pop(-1)

    def top(self) -> int:
        return self.stackList[-1]

"""
Stacks store data in a last-in-first-out order. They're commonly used in coding challenges for sorting and searching problems.
"""

stack = Stack()
nums = [1, 2, 3, 4, 5]
for num in nums:
    stack.push(num)
for i in range(len(nums)):
    print(stack.pop())
