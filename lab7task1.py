class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
        self.n = 0

    def isEmpty (self):
        if self.n == 0:
            return True
        else: return False

    def isFull (self):
        if self.size == self.n:
           return True
        else: return False

    def loadfactor (self):
        return self.n/self.size

    def getHashValue (self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp

    def insert (self,name):
        hashv = self.getHashValue(name) % self.size
        original = hashv
        while self.table[hashv] is not None:
            print('Collision at index',hashv)
            hashv += 1
            if hashv == self.size:
                hashv = 0
            if hashv == original:
                print('Table is Full')
                return False
        self.table[hashv] = name
        self.n += 1
        return True

    def search (self,name):
        hashv = self.getHashValue(name) % self.size
        original = hashv
        while self.table[hashv] != name:
            print('Collision at index',hashv)
            hashv += 1
            if hashv == self.size:
                hashv = 0
            if hashv == original:
                return False
        return True

    def display (self):
        for i in range(self.size):
            a = self.table[i]
            if a is None:
                a = 'Empty'
            print('Index',i, ' = ', a)

    def remove (self,name):
        hashv = self.getHashValue(name) % self.size
        while self.table[hashv] != name:
            print('Collision at index,',hashv)
            hashv += 1
            if hashv == self.size:
                hashv = 0
            if hashv == original:
                return False
        self.table[hashv] = None
        self.n -= 1
        return True

def main():
    size = int(input("Enter the size of Hash Table: "))
    hasht = HashTable(size)

    while True:
        print("\nMenu:")
        print("1. Insert a name")
        print("2. Search for a name")
        print("3. Remove a name")
        print("4. Display the Hash Table")
        print("5. Display Load Factor of the table")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name to insert: ")
            if hasht.insert(name):
                print("Name inserted successfully")
            else:
                print("Failed to insert name")
        elif choice == 2:
            name = input("Enter the name to search: ")
            if hasht.search(name):
                print("Name found in the hash table")
            else:
                print("Name not found in the hash table")
        elif choice == 3:
            name = input("Enter the name to remove: ")
            if hasht.remove(name):
                print("Name removed successfully")
            else:
                print("Name not found in the hash table")
        elif choice == 4:
            hasht.display()
        elif choice == 5:
            print("Load Factor:", hasht.loadfactor())
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()




















