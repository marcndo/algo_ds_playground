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
                    

    
    def lookup(self, value):
        pass


    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            # Only print the right subtree if node.right is not None
            if node.right:  
                self.print_tree(node.right, level + 1)  # Recurse into the right subtree
            print(' ' * 4 * level + '->', node.value)  # Print the current node's value
            # Only print the left subtree if node.left is not None
            if node.left:  
                self.print_tree(node.left, level + 1) 

binary_tree = BinaryTree()
binary_tree.insert(9)
binary_tree.insert(4)
binary_tree.insert(20)
binary_tree.insert(15)
binary_tree.insert(170)
binary_tree.print_tree()