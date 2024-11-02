


def factorialLoop(target: int) -> int:
    result = 1
    for i in range(1, (target + 1)):
        result = result * i
    return result

def factorialRecursion(target: int) -> int:
    if target >= 1:
        return target * factorialRecursion(target - 1)
    else:
        return 1


"""
factorial a mathmatic problem where you multiply a number minus one to zero. 4! = 4 * 3 * 2 * 1 = 24

This is a classic problem to showcase the programming strategy of recursion. I will solve it both using iteration and recursion
"""


nums = 4

print(factorialLoop(nums))

print(factorialRecursion(nums))
