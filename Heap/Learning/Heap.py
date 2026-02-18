class Heap:

    def __init__(self, cap):
        self.size = 0

        self.heap = [0] * cap
    
    def parent(self, ind):

        return (ind -1) //2

    def left_child(self, ind):

        return 2 * ind + 1
    
    def right_child(self, ind):

        return 2 * ind +  2

    def insert(self,value):

        if self.size == len(self.heap):
            print("Heap is full")
            return
        
        self.heap[self.size] = value

        k = self.size
        self.size  += 1
        while k != 0 and self.heap[self.parent(k)] > self.heap[k]:
            self.heap[self.parent(k)], self.heap[k] = self.heap[k], self.heap[self.parent(k)]
            k = self.parent(k)
    
    def heapify(self, ind):

        l1 = self.left_child(ind)
        r1 = self.right_child(ind)

        smallest = ind

        if l1 < self.size and self.heap[l1] < self.heap[smallest]:
            smallest = l1
        
        if r1 < self.size and self.heap[r1] < self.heap[smallest]:
            smallest = r1
        
        if smallest != ind:
            self.heap[smallest], self.heap[ind] = self.heap[ind], self.heap[smallest]
            self.heapify(smallest)

    
    def get_min(self):

        if self.size == 0:
            return float('inf')
        
        return self.heap[0]

    def extract_min(self):

        if self.size == 0:
            return float('inf')
        
        if self.size == 1:
            self.size -= 1
            return self.heap[0]

        mini = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heapify(0)
        return mini
    
    def decrease_key(self, idx, value):

        self.heap[idx] = value

        k = idx
        while k != 0 and self.heap[self.parent(k)] > self.heap[k]:
            self.heap[self.parent(k)], self.heap[k] = self.heap[k], self.heap[self.parent(k)]
            k = self.parent(k)
    
    def delete_key(self, idx):

        self.decrease_key(idx, float('-inf'))
        self.extract_min()
    
    def printHeap(self):

        for i in range(self.size):
            print(self.heap[i], end=" ")
        print()


heap = Heap(15)
arr = [3, 17, 8, 21, 27, 13, 8, 23, 24, 27]
for  i in range(10):
    heap.insert(arr[i])

heap.printHeap()

heap.extract_min()
# heap.printHeap()

# print(heap.get_min())

# heap.delete_key(6)
# heap.printHeap

for i in range(len(arr)):
    print(heap.extract_min())