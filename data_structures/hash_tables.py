class HashTables:
    def __init__(self, size):
        self.data = [None] * size

#the hash function
    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * (i+1)) % len(self.data)
        return hash_value
    
# set values to keys
    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

# get values
    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for i in range(len(self.data)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None

hash_table = HashTables(50)
hash_table.set('name', 'Jane')
hash_table.set('score', 20)
print(hash_table.get('score'))
print(hash_table.get('name'))
