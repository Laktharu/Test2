
# Super Class
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 1


    def is_empty(self):
        if self.head == None:
            print("\n \t  **** This stack is empty! ****")
        else:
            print(" \n \t  ...This stack is not empty!")


    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current . next

        return count


    def push(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None

        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.data
        self.length -= 1

    def top(self):
        if self.is_empty():
            return None

        else:
            return self.head.data

    def display(self):
        currentNode = self.head
        if self.is_empty():
            print(" \n \t Stack Underflow!")

        else:
            while (currentNode != None):
                print(currentNode.data, "--->", end=" ")
                currentNode = currentNode.next
            return
