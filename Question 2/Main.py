from Stack import Stack

s = Stack()
s.push(10)
s.push(22)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
s.push(90)
s.push(100)

print("Size of the stack: ",s.size())
s.display()


print("\n Top element is: ", s.top())

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()

print("Top element is: ", s.top())
print("Size of the stack: ",s.size())
s.display()