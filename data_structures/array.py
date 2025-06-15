class MyArray:

    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return f"{self.data}"
    
    def get_item(self, index):
        return self.data[index]
    
    def push_item(self, item):
        self.data[self.length] = item
        self.length +=1

    def pop_item(self):
        del self.data[self.length -1]
        self.length -= 1

    def delete_item(self, index):
        def shift_items(index):
            for i in range(index, self.length -1):
                self.data[index ] = self.data[i + 1]
        del self.data[self.length -1]
        self.length -=1
        return shift_items(index)
    
    def insert_item(self, index, value):
        for i in range(index, self.length):
            if i == index:
                current_val = self.data[index]
                self.data[index] = value
                next_val = self.data[index + 1]
                self.data[index + 1] = current_val
        self.data[self.length] = next_val
        self.length +=1

# Implement a static array
class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0

    def __str__(self):
        return str(self.data)

    def append(self, value):
        self.data[self.length - 1] = value
        self.length += 1

    def get(self, index):
        for i in range(self.length):
            if i == index:
                return self.data[index]
        return f'No element at index {index}'
    
my_array = MyArray()
my_array.push_item(8)
my_array.push_item(9)
my_array.push_item(6)
my_array.insert_item(1, 20)
my_array.pop_item()
print(my_array)