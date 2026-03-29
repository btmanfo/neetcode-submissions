class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #this is the dummy node to keep track of the left recent value (left) and the most recent value (right)
        self.left, self.right = Node(0,0), Node(0,0)
        #initialy we want these node to be connected to each other
        self.left.next = self.right
        self.right.prev = self.left

    #this is used to remove from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    
    #so this insert at right (because it is the most recent)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            #when we get, we want to remove
            self.remove(self.cache[key])
            #then we want to insert it at the right because it is the most recently used one
            self.insert(self.cache[key])
            return self.cache[key].val
        #if not present, we simply return -1
        return -1


    def put(self, key: int, value: int) -> None:
        #so if the node is already in our cache we want to remove it to update it and put is in the most recent
        if key in self.cache:
            self.remove(self.cache[key])
        #we put it in our hashmap
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #everytime we insert a new value we need to check if we exided the capacity
        if len(self.cache)> self.cap:
            #now we need to remove the most the lest recently used from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
