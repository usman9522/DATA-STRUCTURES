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
        var = self.head
        if var is None:
            return None
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

def isValidated(maze,i,j):
    if maze[x][y] != '*' and 0<x<len(maze) and 0<y<len(maze[0]):
        return True
    else: return False


def solve_maze(maze):
    for i in range(len(maze[0])):
        for j in range (len(maze)):
            if maze[i][j] == 'P':
                stack.push((i,j))

    stack = Stack()
    while stack.isEmpty() is True:
        row, col = stack[-1]

        if maze[row][col] == 'T':
            path = [(r, c) for r, c in stack]
            return "solved", path

        p = stack.pop()
        neighbors_offsets = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    for dr, dc in neighbors_offsets:
        next_row, next_col = row + dr, col + d
        if is_valid_move(maze, next_row, next_col) and (next_row, next_col) not in visited:
            stack.append((next_row, next_col))
            visited.add((next_row, next_col))
            found_next_move = True
            break




def main():
    maze = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", " "]
    ]

    status, path = solve_maze(maze)
    print(status)
    if status == "Solved":
        print("Path:", path)

main()





