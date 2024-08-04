import math
class Student:
    def __init__(self, rollNo, cgpa):
        self.rollNo = rollNo
        self.cgpa = cgpa
class StudentMaxHeap:
    def __init__(self, size):
        self.maxSize = size # Maximum number of students that can be stored in the heap
        self.currSize = 0 # Current number of students present in the heap
        self.students = [None] * size # Array of students which will be arranged like a Max Heap

    def isEmpty(self): # Checks whether the heap is empty or not
        return self.currSize == 0

    def isFull(self): #Checks whether the heap is full or not

        return self.currSize == self.maxSize

    def insert(self, student):
        if self.isFull():
            return False
        self.students[self.currSize] = student
        self.currSize += 1
        self._heapify_up(self.currSize-1)
        return True


    def removeBestStudent(self):
        if not self.students:
            return False
        b = self.students[0]
        self.students[0] = self.students[self.currSize-1]
        self.currSize -= 1
        self._heapify_down(0)
        return b


    def levelOrder(self):
        for i in range(self.currSize):
            print(f'RollNo: {self.students[i].rollNo} , Name: {self.students[i].cgpa}')

    def height(self):
        return math.log2(self.currSize)

    def _heapify_up(self, index):
        p = (index-1)//2
        if index <= 0:
            return
        p_c = self.students[p].cgpa
        i_c = self.students[index].cgpa

        if i_c <  p_c:
            return
        else:
            self.students[p] , self.students[index] = self.students[index] , self.students[p]
            self._heapify_up(p)

    def _heapify_down(self, index):
        l = (index*2) + 1
        r = (index*2) + 2
        if l > self.currSize and r > self.currSize:
            return
        if r > self.currSize and l <= self.currSize:
            if self.students[l].cgpa < self.students[index].cgpa:
                    return
            else:
                self.students[index] , self.students[l] = self.students[l] , self.students[index]
        if r < self.currSize :
            maxi = max(self.students[l].cgpa , self.students[r].cgpa)
            p = self.students[index].cgpa
            if maxi <= p:
                return
            if maxi == self.students[l].cgpa :
                self.students[index] , self.students[l] = self.students[l] , self.students[index]
                self._heapify_down(l)
            else:
                self.students[index] , self.students[r] = self.students[r] , self.students[index]
                self._heapify_down(r)





def main():
    heap = StudentMaxHeap(10)
    heap.insert(Student(1, 3.8))
    heap.insert(Student(2, 3.9))
    heap.insert(Student(3, 3.7))
    heap.insert(Student(4, 4.0))
    heap.levelOrder()
    print(heap.height())
    s = heap.removeBestStudent()
    print(f"Removed Student - Roll No: {s.rollNo}, CGPA: {s.cgpa}")
    s = heap.removeBestStudent()
    print(f"Removed Student - Roll No: {s.rollNo}, CGPA: {s.cgpa}")
    heap.levelOrder()
    print(f"Height of the heap: {heap.height()}")

main()







