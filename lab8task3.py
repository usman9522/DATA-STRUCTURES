import random


class BST:
    class BTNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def add(self, d, t):
        if t is None:
            return self.BTNode(d)
        if t.data > d:
            t.left = self.add(d, t.left)
        elif t.data < d:
            t.right = self.add(d, t.right)
        return t

    def add_node(self, d):
        self.root = self.add(d, self.root)

    def inorder(self, t):
        if t is not None:
            self.inorder(t.left)
            print(t.data, end=' ')
            self.inorder(t.right)

    def inorder_traversal(self):
        self.inorder(self.root)
        print()

    def preorder(self, t):
        if t is not None:
            print(t.data, end=' ')
            self.preorder(t.left)
            self.preorder(t.right)

    def preorder_traversal(self):
        self.preorder(self.root)
        print()

    def count_nodes(self, t):
        if t is None:
            return 0
        return 1 + self.count_nodes(t.left) + self.count_nodes(t.right)

    def inorder_array(self, t, array, index):
        if t is not None:
            index = self.inorder_array(t.left, array, index)
            array[index] = t.data
            index += 1
            index = self.inorder_array(t.right, array, index)
        return index

    def add_binary_search(self, array, start, end):
        if start <= end:
            mid = (start + end) // 2
            self.add_node(array[mid])
            self.add_binary_search(array, start, mid - 1)
            self.add_binary_search(array, mid + 1, end)


    def check_and_balance_tree(self, count_nodes):
        array_size = count_nodes + 1
        array = [0] * array_size
        self.inorder_array(self.root, array, 0)
        self.remove_nodes(self.root)
        self.add_binary_search(array, 0, len(array) - 1)


    def check_and_balance(self):
        left_c = self.count_nodes(self.root.left)
        right_c = self.count_nodes(self.root.right)
        difference = abs(left_c - right_c)
        if difference > 1:
            self.check_and_balance_tree(self.count_nodes(self.root))


    def remove_nodes(self, t):
        if t is not None:
            self.remove_nodes(t.left)
            self.remove_nodes(t.right)
            del t


    def __del__(self):
        self.remove_nodes(self.root)


if __name__ == "__main__":
    tree = BST()
    for _ in range(20):
        tree.add_node(random.randint(100, 999))
    print('preorder traversal:')
    tree.preorder_traversal()
    print('inorder traversal:')
    tree.inorder_traversal()
    print('check and balance:')
    tree.check_and_balance()
    print('preorder traversal:')
    tree.preorder_traversal()
    print('inorder traversal:')
    tree.inorder_traversal()
