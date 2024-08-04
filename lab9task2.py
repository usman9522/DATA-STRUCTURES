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




    def _heapify_up(self, index):
        p = (index-1)//2
        if index <= 0:
            return
        p_c = self.students[p]
        i_c = self.students[index]

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
            if self.students[l]< self.students[index]:
                    return
            else:
                self.students[index] , self.students[l] = self.students[l] , self.students[index]
        if r < self.currSize :
            maxi = max(self.students[l] , self.students[r])
            p = self.students[index]
            if maxi <= p:
                return
            if maxi == self.students[l] :
                self.students[index] , self.students[l] = self.students[l] , self.students[index]
                self._heapify_down(l)
            else:
                self.students[index] , self.students[r] = self.students[r] , self.students[index]
                self._heapify_down(r)





def main():
    heap = StudentMaxHeap(10)
    a = []
    b = int(input('enter length of list: '))
    while True:
        x = int(input('enter element: '))
        a.append(x)
        if len(a) == b:
            break

    for i in range(b):
        heap.insert(a[i])
    us = heap.removeBestStudent()
    ha = heap.removeBestStudent()
    print(us,ha)
    print((us-1)*(ha-1))


main()







