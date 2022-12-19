stack = []

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
stack.append('F')

print(f"sliced: {stack[:]}")

item = stack.pop()
print(f"Item poped = {item}")
print(stack)
for i in range(10):
    if len(stack) > 0:
        stack.pop()
print(stack)