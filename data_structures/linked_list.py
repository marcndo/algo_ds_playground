class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    
    def delete(self, key):
        """Delete the first occurrence of a node by key."""
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the list
        if not current:
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    def prepend(self, data):
        """Add a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, position, data):
        """
        Insert a new node at a specific position in the list.
        Position is zero-based:
        - 0 to insert at the beginning
        - len(list) to append to the end
        """
        if position < 0:
            raise ValueError("Position must be a non-negative integer.")
        
        new_node = Node(data)
        # Insert at the head
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        # Traverse the list to find the insertion point
        while current and count < position - 1:
            count += 1
            current = current.next
        # If position is beyond the length of the list
        if not current:
            raise IndexError("Position out of bounds.")
        # Insert the new node
        new_node.next = current.next
        current.next = new_node
    
    def __repr__(self):
        """Return a string representation of the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

linked_list = LinkedList()

# Append nodes
linked_list.append(10)
linked_list.append(20)
linked_list.append(30) 
linked_list.append(50)
linked_list.insert(2, 9)
print(linked_list)
linked_list.prepend(123)
linked_list.delete(30)
print(linked_list)