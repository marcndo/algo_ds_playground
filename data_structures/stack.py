class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

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

# A simplier version of stack
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            holding_pointer = self.head
            self.head = new_node
            new_node.next = holding_pointer

    def pop(self):
        if not self.head:
            return None
        else:
            holding_pointer = self.head
            self.head = self.head.next

    def peek(self):
        return self.head.data

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "->".join(nodes)

stack = Stacks()
stack.push_item(4)
stack.push_item(9)
stack.push_item(8)
print(stack.peek())
 # stack.pop()
print(stack)
stack = Stack()
stack.push('Jude')
stack.push('Merveille')
stack.push('Jean')
stack.push('Laura')
stack.push('Jeremy')
stack.pop()
stack.pop()
print(stack.peek())
print(stack)

