

# 155 min-stack

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.



"""
class MinStack:

    def __init__(self):
        self.stackList = []
        self.rollingMin = []

    def push(self, val: int) -> None:
        self.stackList.append(val)

        #Update rollingMin
        if not self.rollingMin:
            self.rollingMin.append(val)
        elif val < self.rollingMin[-1]:
            self.rollingMin.append(val)
        else:
            self.rollingMin.append(self.rollingMin[-1])

    def pop(self) -> None:
        self.stackList.pop(-1)
        self.rollingMin.pop(-1)


    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return self.rollingMin[-1]    
    


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
val = -2
obj.push(val)
val = 0
obj.push(val)
val = -3
obj.push(val)
param_4 = obj.getMin()
print(param_4)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)

# Assumption made that top is view only and not popping the value
