class HashTable2:
    ''' Makes use of chain of elements (lists) to handle collisions
    Supports both int and str
    '''

    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [[] for x in range(self.size)]

    def binary_search(self, alist, aitem):
        lb = 0
        ub = len(alist)
        while True:
            if lb == ub:
                return -1
            mid = (lb + ub) // 2
            item_at_mid = alist[mid]
            if item_at_mid == aitem:
                return mid
            elif item_at_mid < aitem:
                lb = mid + 1
            else:
                ub = mid

    def linear_search(self, alist, aitem):
        for k, v in enumerate(alist):
            if v == aitem:
                return k
        return -1

    def hash_function(self, key, size):
        if isinstance(key, int):
            return key%size
        elif isinstance(key, str):
            asum = 0
            for pos in range(len(key)):
                asum += (ord(key[pos]) * pos)
        return asum%size

    def rehash(self, oldhash, size):
        return (oldhash+3)%size

    def put(self, key, data):
        # Chaining to handle collisions

        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            if self.data[hash_value] == []:
                self.data[hash_value].append(data)
            else:
                position = self.linear_search(self.data[hash_value], data)
                if position < 0:
                     self.data[hash_value].append(data)
                else:
                     self.data[hash_value][position] = data
        else:
            if self.slots[hash_value] == key:
                position = self.linear_search(self.data[hash_value], data)
                if position < 0:
                     self.data[hash_value].append(data)
                else:
                     self.data[hash_value][position] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                     next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                     self.slots[next_slot] = key
                     if self.data[next_slot] == []:
                         self.data[next_slot].append(data)
                     else:
                         position = self.linear_search(self.data[next_slot], data)
                         if position < 0:
                             self.data[next_slot].append(data)
                         else:
                             self.data[next_slot][position] = data

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        found = False
        stop = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                next_slot = self.rehash(position, len(self.slots))
                if position == start_slot:
                     stop = True
        return data
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key, data)
