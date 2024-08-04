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
        var = self.head
        if var is None:
            return None
        return self.head.data

    def stack_size(self):
        return f'Size of Stack is: {self.size}'

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

def reverseWords():
    stack = Stack()
    a = input().split()
    for i in range(len(a)):
        for j in range(len(a[i])):
            stack.push(a[i][j])
        while stack.peek() is not None:
            print(stack.pop(),end='')
        print(end=' ')


def main():
    reverseWords()

main()

















