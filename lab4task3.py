class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__ (self,size):
        self.head = None
        self.size = size
        self.count = 0

    def enque(self,data):
        new_node = Node(data)
        if self.count < self.size:

            if self.head is None:
                self.head = new_node
                self.count += 1
            else:
                var = self.head
                while var.next is not None:
                    var = var.next
                var.next = new_node
                self.count += 1
        elif self.count == 7:
            var = self.head
            while var.next is not None:
                if var.next is None:
                    var.next = new_node
                    new_node.next = self.head
            self.count += 1

        else:
            print('Element is not added because Queue is full')

    def deque(self):
        pre = self.head
        self.head = self.head.next
        self.count -= 1
        return f'Dequed element is: {pre.data}'

    def front(self):
        return self.head.data

    def sizee(self):
        return self.size

    def isEmpty(self):
        if self.head is None:
            return 'Stack is Empty'
        else: return 'Stack contain Elements'

    def isFull(self):
        if self.size == self.count:
            return 'Queue is Full'
        else: return 'Queue is not full'

    def display(self):
        var = self.head
        while var is not None:
            print(var.data,end=' => ')
            var = var.next
        print()

def main():
    queue = Queue(8)
    queue.enque(14)
    queue.enque(22)
    queue.enque(13)
    queue.enque(-6)
    queue.display()
    print("Deleted value = ", queue.deque())
    print("Deleted value = ", queue.deque())
    queue.display()
    queue.enque(9)
    queue.enque(20)
    queue.enque(5)
    queue.display()




main()

