class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def enque(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            var = self.tail
            var.next = new_node
            self.tail = new_node
            self.size += 1

    def deque(self):
        pre = self.head
        self.head = self.head.next
        self.size -= 1
        return pre.data

    def front(self):
        return self.head.data

    def queue_size(self):
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

def main():
    queue = Queue()
    queue.enque(5)
    queue.enque(6)
    queue.enque(7)
    queue.enque(8)
    queue.enque(9)
    queue.enque(10)
    queue.display()
    print(queue.deque())
    print(queue.front())
    queue.display()
    print(queue.queue_size())


main()

