from MyStack import MyStack

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(str(stack.peek()))
stack.push(4)
stack.push(5)
stack.push(6)
print(str(stack.peek()))
print(str(stack))
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(str(stack.peek()))
print(str(stack))