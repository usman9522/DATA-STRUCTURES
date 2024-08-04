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
        if self.head is None:
            return None
        else: return self.head.data

    def stack_size(self):
        return f'Size of Stack is: {self.size}'

    def isEmpty(self):
        if self.head is None:
            return True
        else: return False

def parenthesis(s):
    stack = Stack()
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.push(i)
        elif (i == ')' and stack.peek() == '(') or (i == '}' and stack.peek() == '{') or (i == ']' and stack.peek() == '['):
            stack.pop()
        elif (i == ')' and stack.peek() != '(') or (i == '}' and stack.peek() != '{') or (i == ']' and stack.peek() != '['):
            return False
    return stack.isEmpty()


print(parenthesis('()(){}{[][}[]'))
