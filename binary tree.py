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

class BinaryTree:
    def __init__(self):
        self.root = None
        self.total = 0

    def insert_element_root(self, element):
        node = Node(element)
        if self.root is None:
            self.root = node
            self.total += 1
        else:
            return

    def insert_left_child(self, parent, child):
        node = Node(child)
        if parent is None:
            return
        if parent.left is not None:
            return
        parent.left = node
        self.total += 1

    def insert_right_child(self, parent, child):
        node = Node(child)
        if parent is None:
            return
        if parent.right is not None:
            return
        parent.right = node
        self.total += 1

    def delete_element(self, element):
        if self.root is None:
            return
        a = [self.root]
        while a:
            curr = a.pop(0)
            if curr.value == element:
                curr.value = None
                self.total -= 1
                return
            if curr.left:
                a.append(curr.left)
            if curr.right:
                a.append(curr.right)


    def count_nodes(self):
        return self.total

    def display_pre_order(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.display_pre_order(node.left)
        self.display_pre_order(node.right)

    def display_in_order(self, node):
        if node is None:
            return
        self.display_in_order(node.left)
        print(node.value, end=' ')
        self.display_in_order(node.right)

    def display_post_order(self, node):
        if node is None:
            return
        self.display_post_order(node.left)
        self.display_post_order(node.right)
        print(node.value, end=' ')

    def min_value(self, node):
        if node is None:
            return None
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)

    def non_rec_pre_order(self):
        if self.root is None:
            return
        a = [self.root]
        while a:
            curr = a.pop()
            print(curr.value, end=' ')
            if curr.right:
                a.append(curr.right)
            if curr.left:
                a.append(curr.left)

    def non_rec_post_order(self):
        if self.root is None:
            return
        a = [self.root]
        b = []
        while a:
            curr = a.pop()
            b.append(curr)
            if curr.left:
                a.append(curr.left)
            if curr.right:
                a.append(curr.right)
        while b:
            print(b.pop().value, end=' ')

    def non_rec_in_order(self):
        if self.root is None:
            return
        a = []
        curr = self.root
        while a or curr:
            while curr:
                a.append(curr)
                curr = curr.left
            curr = a.pop()
            print(curr.value, end=' ')
            curr = curr.right

    def height_of_tree(self, node):
        if node is None:
            return 0
        height = 0
        a = [(node, 1)]
        while a:
            curr, level = a.pop()
            height = max(height, level)
            if curr.right:
                a.append((curr.right, level + 1))
            if curr.left:
                a.append((curr.left, level + 1))
        return height

    def find_balance_factor(self, node):
        if node is None:
            return 0
        left = self.height_of_tree(node.left)
        right = self.height_of_tree(node.right)
        return left - right

    def display_ancestors(self, node_data):
        if self.root is None:
            return
        a = [(self.root, [])]
        found = False
        while a:
            curr, p = a.pop()
            if curr.value == node_data:
                print("Ancestors are", p)
                found = True
                break
            if curr.right:
                a.append((curr.right, p + [curr.value]))
            if curr.left:
                a.append((curr.left, p + [curr.value]))
        if not found:
            return

    def display_descendants(self, node_data):
        if self.root is None:
            return
        node = self.root
        found = False
        a = [node]
        while a:
            curr = a.pop()
            if curr.value == node_data:
                found = True
                break
            if curr.right:
                a.append(curr.right)
            if curr.left:
                a.append(curr.left)
        if not found:
            return
        b = [curr]
        print("Descendants are:")
        while b:
            curr = b.pop(0)
            print(curr.value, end=' ')
            if curr.left:
                b.append(curr.left)
            if curr.right:
                b.append(curr.right)
        print()




def main():
    tree = BinaryTree()
    tree.insert_element_root(7)
    parent = tree.root
    tree.insert_left_child(parent, 6)
    tree.insert_right_child(parent, 10)
    print(tree.count_nodes())
    #tree.delete_element(6)
    #print(tree.count_nodes())
    tree.display_pre_order(tree.root)
    print()
    tree.display_in_order(tree.root)
    print()
    tree.display_post_order(tree.root)
    print()
    print(tree.min_value(parent))
    print(tree.count_leaf_nodes(parent))
    tree.non_rec_pre_order()
    print()
    tree.non_rec_in_order()
    print()
    tree.non_rec_post_order()
    print()
    print(tree.height_of_tree(parent))
    print(tree.find_balance_factor(parent))
    #tree.display_descendants(7)
    #tree.display_ancestors(6)

main()
