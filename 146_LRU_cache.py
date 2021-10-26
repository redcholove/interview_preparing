class DLinked:
    def __init__(self):
        self.key = None
        self.val = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.maxSize = capacity
        self.size = 0
        self.head, self.tail = DLinked(), DLinked()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        sec = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        sec.prev = node
        node.next = sec
    
    def removeNode(self, node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
        node.prev = None
        node.next = None
    
    def get(self, key: int) -> int:
        #check key
        node = self.cache.get(key, None)
        if node:
            self.removeNode(node)
            self.addNode(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #check key
        node = self.cache.get(key, None)
        
        if node:
            self.removeNode(node)
            self.addNode(node)
            node.val = value
        else:
            node = DLinked()
            node.key = key
            node.val = value
            self.addNode(node)
            self.cache[key] = node
            self.size += 1
            
            if self.size > self.maxSize:
                bottom = self.tail.prev
                self.removeNode(bottom)
                del self.cache[bottom.key]
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
