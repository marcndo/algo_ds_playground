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
    
    #get keys
    def get_keys(self):
        keys = []
        for i in range(len(self.data)):
            if self.data[i]:
                keys.append(self.data[i][0][0])
        return keys
    
    #Get values
    def get_values(self):
        values = []
        for i in range(len(self.data)):
            if self.data[i]:
                values.append(self.data[i][0][1])
        return values
    

hash_table = HashTables(50)
hash_table.set('name', 'Jane')
hash_table.set('score', 20)
hash_table.set('age', 28)
hash_table.set('department', 'Mathematics')
hash_table.set('course', 'MAT301')
print(hash_table.get('score'))
print(hash_table.get('name'))
print(hash_table.get_keys())
print(hash_table.get_values())