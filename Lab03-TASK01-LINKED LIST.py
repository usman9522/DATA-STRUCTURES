class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def insert_at_head(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_at_tail(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end=' => ')
            current = curren.next


def main():
    obj = LinkedList()
    obj.insert_at_tail(5)


main()


