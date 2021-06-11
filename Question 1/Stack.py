import numpy as np


# print(newArray)

class Stack_numPy:
    def __init__(self, limit=5):

        self.limit = limit
        self.stack = np.array([])

    def push(self, data):
        if len(self.stack) < self.limit:

            self.stack = np.append(self.stack, data)
            return self.stack

        else:
            print("Stack Overflow")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow!")

        else:
            self.stack = np.delete(self.stack, -1)
            return self.stack

    def top(self):
        if len(self.stack) == 0:
            print("Stack Underflow!")

        else:
            return self.stack[len(self.stack) - 1]

    def is_emptyStack(self):
        return len(self.stack) == 0

    def is_fullstack(self):
        return len(self.stack) == self.limit

    def size(self):
        return len(self.stack)
