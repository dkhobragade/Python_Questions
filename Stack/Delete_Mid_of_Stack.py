stack = [10, 20, 30, 40, 50]

n = len(stack) // 2 - 1
if len(stack) % 2 != 0:
    n = len(stack) // 2

stack.remove(stack[n])
print(stack)
