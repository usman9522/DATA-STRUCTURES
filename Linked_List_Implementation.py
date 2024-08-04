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

    def remove_from_head(self):
        self.head = self.head.next

    def remove_after(self,key):
        var = self.head
        while  var.next is not None:
            if var.data == key:
                var.next = var.next.next
                return
            var = var.next

    def remove_before(self,key):
        var = self.head
        pre = None
        while var.next is not None:
            if var.next.data == key:
                pre.next = var.next
                return
            pre = var
            var = var.next

    def update(self,key,value):
        var = self.head
        while var.next is not None:
            if var.data == key:
                var.data = value
                return
            var = var.next

    def search(self,key):
        var = self.head
        while var is not None:
            if var.data == key:
               return True
            var = var.next
        return False

    def removekth(self,k):
        if k == 1:
            self.head = self.head.next

        var = self.head.next
        a = 2
        pre = self.head
        while var is not None:
            if k == a:
                pre.next = var.next
                return
            pre = var
            a += 1
            var = var.next
        if a <= k:
            return False

    def combine(self,list1,list2):
        var = list1.head
        self.head = var
        while var.next is not None:
            var = var.next
        var.next = list2.head
        list2.head = None
        list1.head = None


    def shuffleMerge(self, list1, list2):
        if list1.head is None and list2.head is None:
            return

        current1 = list1.head
        current2 = list2.head

        self.head = current1


        while current1 is not None and current2 is not None:
            next1 = current1.next
            next2 = current2.next
            current1.next = current2
            current2.next = next1


            current1 = next1
            current2 = next2
        list1.head = None
        list2.head = None





    def reverse(self):
        var = self.head
        pre = None
        while var is not None:
            nextn = var.next
            var.next = pre
            pre = var
            var = nextn
        self.head = pre

    def remove_duplicates1(self):
        var = self.head
        a = var.next
        while var.next is not None:
            if var.data == a.data:
                a = a.next
                var.next = a
            else:
                var = var.next
                a = a.next

    def remove_duplicates(self):
        a = []
        var = self.head
        pre = None
        while var is not None:
            if var.data in a:
                pre.next = var.next
            else:
                a.append(var.data)
                pre = var
            var = var.next







    def display(self):
        var = self.head
        while var is not None:
            print(var.data,end=' => ')
            var = var.next
        print()

def main():
    lis = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()
    lis.insert_at_head(9)
    lis.insert_at_tail(10)
    lis.insert_at_tail(11)
    lis.insert_at_tail(12)
    lis.insert_at_tail(13)
    lis.insert_at_tail(15)
    lis.insert_at_tail(16)
    lis.insert_at_tail(17)
    lis.insert_at_tail(18)
    lis.insert_at_tail(20)
    #lis.display()
    lis.insert_after(13,14)
    lis.insert_before(20,19)
    lis.remove_from_tail()
    lis.remove_from_head()
    #lis.display()
    lis.remove_after(13)
    lis.remove_before(13)
    #lis.display()
    lis.update(10,90)
    #lis.display()
    #print(lis.search(19))
    #print(lis.removekth(9))
    #lis.display()
    list2.insert_at_tail(100)
    list2.insert_at_tail(110)
    list2.insert_at_tail(120)
    list2.insert_at_tail(130)
    lis.display()
    list2.display()
    list3.combine(lis,list2)
    list3.display()
    lis.display()
    list2.display()
    #list2.display()
    #list3.shuffleMerge(lis,list2)
    #list3.display()
    listd = LinkedList()
    listd.insert_at_head(20)
    listd.insert_at_tail(20)
    listd.insert_at_tail(120)
    listd.insert_at_tail(11)
    listd.insert_at_tail(128)
    listd.insert_at_tail(128)
    listd.insert_at_tail(165)
    listd.insert_at_tail(165)
    #listd.display()
    listd.remove_duplicates()
    #listd.display()
main()












