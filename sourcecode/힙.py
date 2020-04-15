class Heap:
    def __init__(self, data):
        self.heap = list()
        self.heap.append(None)
        self.heap.append(data)
    
    def is_move(self, idx):
        if idx <= 1:
            return False
        
        parent_idx = idx // 2
        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False
    
    def insert(self, data):
        if len(self.heap) == 0:
            self.heap.append(None)
            self.heap.append(data)
            return True
        else:
            self.heap.append(data)

            idx = len(self.heap) - 1

            while self.is_move(idx):
                parent_idx = idx // 2
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            
            return True

heap = Heap(1)

heap.insert(10)
heap.insert(7)
heap.insert(3)
heap.insert(66)

print(heap.heap)