#implement the delete method
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node  # Fixed: current_node.left instead of self.left
                        break
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node  # Fixed: current_node.right instead of self.right
                        break
                    current_node = current_node.right

    def lookup(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def breadth_first_search(self):
        current_node = self.root
        list = []
        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue[0]
            del queue[0]
            list.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return list

