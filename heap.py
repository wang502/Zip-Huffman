from swap import swap
#from compress import *

def less(x, y):
    return x < y

def less_key(x, y):
    return x.key < y.key

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * (i + 1)

def parent(i):
    return (i-1) / 2

# Student code -- fill in all the methods that have pass as the only statement
class Heap:
    def __init__(self, data, 
                 less = less):
        self.data = data
        self.less = less
        self.build_min_heap()
        
    def __repr__(self):
        return repr(self.data)
    
    def minimum(self):
        return self.data[0]

    def insert(self, obj):
        self.data.append(obj)
        i = parent(len(self.data)-1)
        while i >= 0:
            self.min_heapify(i)
            i = parent(i)

    def extract_min(self):
        mini = self.data.pop(0)
        self.build_min_heap()
        return mini
        
    def min_heapify(self, i):
        mini = 0
        if left(i) < len(self.data) and less_key(self.data[left(i)], self.data[i]):
            mini = left(i)
        else:
            mini = i
        if right(i) < len(self.data) and less_key(self.data[right(i)], self.data[i]):
            mini = right(i)
        if mini != i:
            swap(self.data, i, mini)
            self.min_heapify(mini)
    
    def build_min_heap(self):
        last_parent = len(self.data)/2-1
        for i in range(last_parent, -1, -1):
            self.min_heapify(i)
    
class PriorityQueue:
    def __init__(self, less=less_key):
        self.heap = Heap([], less)

    def __repr__(self):
        return repr(self.heap)

    def push(self, obj):
        self.heap.insert(obj)

    def pop(self):
        return self.heap.extract_min()

if __name__ == "__main__":
    # unit tests here
    # to run the unit test, uncommand #from compress import *
    # python heap.py
    h1 = Heap([],less)
    n1 = HTreeNode(10, 'A')
    n2 = HTreeNode(4,'C')
    n3 = HTreeNode(2,'D')
    n4 = HTreeNode(6, 'E')
    h1.insert(n1)
    h1.insert(n2)
    h1.insert(n3)
    h1.insert(n4)
    assert h1.extract_min() == n3     # output: 'D': 2
    assert h1.minimum() == n2        # output: 'C': 4
    assert h1.data == [n2, n4, n1]   # output: ['C': 4, 'E': 6, 'A': 10]
    pass