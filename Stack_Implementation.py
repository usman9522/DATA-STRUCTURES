class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__ (self):
        self.head = None
        self.size = 0

    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            pre = self.head
            self.head = self.head.next
            self.size -= 1
            return pre.data

    def peek(self):
        return self.head.data

    def stack_size(self):
        return self.size

    def isEmpty(self):
        if self.head is None:
            return True
        else: return False

    def display(self):
        var = self.head
        while var is not None:
            print(var.data,end=' => ')
            var = var.next
        print()

def reverse_string(s):
    a = Stack()
    s = s.split()
    for i in s:
        for j in i:
            a.push(j)
        while a.isEmpty() is not True:
            print(a.pop(),end='')
        print(end=' ')
reverse_string('welcome to pakistan')



def main():
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    stack.display()
    print(stack.pop())
    print(stack.peek())
    stack.display()
    print(stack.stack_size())


#main()

