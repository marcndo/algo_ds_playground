class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class Stacks:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push_item(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
        self.length +=1
        return self

    def __str__(self):
        # Start at the top of the stack and iterate through the nodes
        current = self.top
        stack_values = []
        while current:
            stack_values.append(str(current))  # Append the value of each node
            current = current.next
        return f"top: {' -> '.join(stack_values)}\nbottom: {self.bottom}\nlength: {self.length}"


    
    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            return None
        else:
            holding_pointer = self.top
            self.top = self.top.next
        self.length -=1

stack = Stacks()
stack.push_item(4)
stack.push_item(9)
stack.push_item(8)
stack.pop()
print(stack)

