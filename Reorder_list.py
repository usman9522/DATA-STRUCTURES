class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        var = self.head
        while var.next is not None:
            var = var.next
        var.next = new_node


    def insert_after(self,key,data):
        new_node = Node(data)
        var = self.head
        while var.next is not None:
            if var.data == key:
                new_node.next = var.next
                var.next = new_node
            var = var.next

    def insert_before(self,key,data):
        new_node = Node(data)
        var = self.head
        while var.next is not None:
            if var.next.data == key:
                new_node.next = var.next
                var.next = new_node
                return
            var = var.next

    def remove_from_tail(self):
        var = self.head
        while var.next.next is not None:
            var = var.next
        var.next = None

    def reverse(self):
        var = self.head
        pre = None
        while var is not None:
            nextn = var.next
            var.next = pre
            pre = var
            var = nextn
        self.head = pre

    def aaa(self):
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        lis = []
        while slow is not None:
            lis.append(slow.data)
            slow = slow.next
        print(lis)
        var = self.head
        while var is not None:
            var.next = lis.pop()
            var = var.next




    def display(self):
        var = self.head
        while var is not None:
            print(var.data,end=' => ')
            var = var.next
        print()

def main():
    lis = LinkedList()
    lis.insert_at_head(10)
    lis.insert_at_tail(11)
    lis.insert_at_tail(12)
    lis.insert_at_tail(13)
    lis.display()
    lis.insert_after(12,34)
    lis.insert_before(12,24)
    lis.remove_from_tail()
    lis.display()
    lis.reverse()
    lis.display()
    lis.aaa()

main()













