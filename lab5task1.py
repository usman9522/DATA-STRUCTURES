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
            return 'Stack is empty'
        else:
            pre = self.head
            self.head = self.head.next
            self.size -= 1
            return pre.data

    def peek(self):
        if self.head is not None:
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

def convertToPostfix(exp):
    stack = Stack()
    for i in exp:
        if i == '(':
            stack.push(i)
        elif i == '+' or i == '-':
            stack.push(i)
        elif i == '+' and stack.peek() == '-':
            print(stack.pop(),end='')
        elif i == '*' and stack.peek() == '/':
            print(stack.pop(),end='')
        elif (i == '/' or i== '*')  and (stack.peek() == ')') :
            stack.push(i)
        elif i == ')':
            print(stack.pop(),end='')
            while stack.peek() != '(':
                stack.pop()
            stack.pop()
        else:
            print(i,end='')

    while stack.isEmpty() is False:
        print(stack.pop(),end='')

convertToPostfix('3+4*5/6')









