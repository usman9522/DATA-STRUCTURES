class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__ (self):
        self.head = None
        self.min = []


    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        if not self.min  or data <= self.min[-1] :
            self.min.append(data)


    def pop(self):
        if self.head is None:
            return None
        else:
            pre = self.head
            self.head = self.head.next
            if pre.data == self.min[-1]:
                self.min.pop()
            return pre.data

    def peek(self):
        if self.head is None:
            return None
        else: return self.head.data

    def getMin(self):
        return self.min[-1]

    def display(self):
        var = self.head
        while var is not None:
            print(var.data,end=' => ')
            var = var.next
        print()

def main():
    stack = Stack()
    stack.push(53434)
    stack.push(34)
    stack.push(7)
    stack.push(785)
    stack.push(-3435)
    stack.push(-45)
    stack.display()
    stack.pop()
    stack.pop()
    stack.display()
    print(stack.peek())
    print(stack.getMin())





main()
