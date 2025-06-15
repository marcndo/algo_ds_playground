"""
LinkedList: A data structure that stores data in a way that each data point
is linked to the another data point.
Each data entry contains its data point and address to the next data point
The main operations in this data structure include
prepend, append ---> O(1), Insert, delete, access O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return "->".join(nodes)

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            holding_pointer = self.head
            self.head = new_node
            new_node.next = holding_pointer

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            count = 0
            holding_pointer = self.head
            while count < position:
                prev = holding_pointer
                holding_pointer = holding_pointer.next
                count += 1
            new_node.next = holding_pointer
            prev.next = new_node

    def delete(self, data):
        if not self.head:
            return None
        holding_pointer = self.head
        while holding_pointer and holding_pointer.data != data:
            prev = holding_pointer
            holding_pointer = holding_pointer.next
        prev.next = holding_pointer.next

    def get(self, data):
        if not self.head:
            return None
        holding_pointer = self.head
        while holding_pointer and holding_pointer.data != data:
            holding_pointer = holding_pointer.next
        if not holding_pointer:
            return None
        return holding_pointer.data


linked_list = LinkedList()
# linked_list.prepend('Jane')
# linked_list.prepend('Jude')
# linked_list.prepend('Jack')
# linked_list.prepend('Paula')
linked_list.append('Janifer')
linked_list.append('Peter')
linked_list.append('Meivelle')
linked_list.insert('Julia',2)
linked_list.insert('Morgan', 3)
linked_list.insert('Aisa', 4)
linked_list.delete('Peter')
print(linked_list.get('Meivelle'))
print(linked_list)
linked_list.append('James')
linked_list.append('Jeremiah')
print(linked_list)
