class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# [1, 3, 2, 5]

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            # If the queue is empty, return None or an appropriate message
            print("Queue is empty")
            return None
        else:
            dequeued_data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return dequeued_data

    def peek(self):
        return self.head.data

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "->".join(nodes)


queue = Queue()
queue.enqueue(7)
queue.enqueue(9)
queue.enqueue(89)
queue.enqueue(90)
queue.dequeue()
print(queue.peek())
print(queue)
