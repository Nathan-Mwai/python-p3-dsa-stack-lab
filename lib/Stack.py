class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
        
    def full(self):
        return len(self.items) == self.limit


    def push(self, item):
        self.items.append(item) if not self.full() else None


    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None
    
    def size(self):
        return len(self.items)
        
    def search(self, target):
        reverse_items = self.items[::-1]
        for num in range(len(reverse_items)):
            if reverse_items[num] == target:
                return num
        return -1
            
