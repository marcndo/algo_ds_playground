class MyArray:

    def __init__(self):
        self.length = 0
        self.data = {}

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
