from Stack import Stack_numPy

myStack = Stack_numPy()
print(myStack.push(100))
print(myStack.push(20))
print(myStack.push(35))
print(myStack.push(7777))
print(myStack.push(111))

print(myStack.pop())

print("\n \t Waiting in Top: ", myStack.top())

print("\n \t Is this stack in empty?.... ", myStack.is_emptyStack())

print("\n \t Is this Stack in full?.... ",myStack.is_fullstack())

print("\n \t Size of Stack: ", myStack.size())

