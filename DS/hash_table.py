class HashTable:

    def __init__(self):
        self.size = 11  # prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace

            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def hash_function(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def main():
    ht = HashTable()

    ht.put(1, 10)
    ht.put(6, 'test')
    ht.put(8, 2.5)
    ht.put(2, 20)
    ht.put(3, 25)
    ht.put(4, 60)
    ht.put(7, 24)
    ht.put(9, 0)
    ht.put(5, 100.0)
    ht.put(11, 'google')
    ht.put(10, 'yahoo')

    ht.get(10)
    ht.get(11)
    ht.get(3)

    print(ht.data)
    print(ht.slots)

if __name__ == '__main__':
    import cProfile
    cProfile.run("main()")
