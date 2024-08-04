 import random
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def set_value(self, value):
        self.value = value
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def get_value(self):
        return self.value
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.total = 0

    def insert_element(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.total += 1
            return
        else:
            curr = self.root
            while True:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = node
                        self.total += 1
                        break
                    else:
                        curr = curr.left

                elif value > curr.value:
                    if curr.right is None:
                        curr.right = node
                        self.total += 1
                        break
                    else:
                        curr = curr.right
                else:
                    break

    def delete_element(self, value):
        parent = None
        curr = self.root

        while curr:
            if value == curr.value:
                if curr.left is None:
                    if parent:
                        if parent.left == curr:
                            parent.left = curr.right
                        else:
                            parent.right = curr.right
                    else:
                        self.root = curr.right
                    self.total -= 1
                    return
                elif curr.right is None:
                    if parent :
                        if parent.left == curr:
                            parent.left = curr.left
                        else:
                            parent.right = curr.left
                    else:
                        self.root = curr.left
                    self.total -= 1
                    return

                succ_parent = curr
                succ = curr.right
                if succ.left is None:
                    curr.value = succ.value
                    curr.right = succ.right
                    self.total -= 1
                    return
                else:
                    while succ.left:
                        succ_parent = succ
                        succ = succ.left
                    curr.value = succ.value
                    succ_parent.left = succ.right
                    self.total -= 1
                    return

            elif value < curr.value:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right


    def display_pre_order(self):
        if self.root is None:
            return

        a = []
        a.append(self.root)

        while a :
            curr = a.pop()
            print(curr.value,end=' ')

            if curr.right:
                a.append(curr.right)
            if curr.left:
                a.append(curr.left)
        print()

    def display_in_order(self):
        if self.root is None:
            return

        a = []
        curr = self.root

        while True:
            if curr is not None:
                a.append(curr)
                curr = curr.left
            elif a:
                curr = a.pop()
                print(curr.value, end=' ')
                curr = curr.right
            else:
                break
        print()
    def display_post_order(self):
        if self.root is None:
            return
        a = []
        b = []
        a.append(self.root)
        while a:
            curr = a.pop()
            b.append(curr)
            if curr.left:
                a.append(curr.left)
            if curr.right:
                a.append(curr.right)
        while b:
            print(b.pop().value, end=' ')
        print()

    def total_elements(self):
        return self.total


def main():
    tree = BinarySearchTree()
    for i in range(10):
        a = random.randint(10,100)
        tree.insert_element(a)
    for i in range(10):
        a = random.randint(10,100)
        tree.delete_element(a)
    tree.display_pre_order()
    tree.display_in_order()
    tree.display_post_order()
    print(tree.total_elements())

main()


