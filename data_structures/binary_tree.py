class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    return
                else:
                    current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def get(self,value):
        current = self.root
        if not current:
            return False
        while True:
            if current.value == value:
                return value
            elif value < current.value:
                current = current.left
            else:
                current = current.right


    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
        # Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)


binary_tree = BinarySearchTree()
binary_tree.insert(9)
binary_tree.insert(2)
binary_tree.insert(1)
binary_tree.insert(20)
print(binary_tree.get(20))
print(binary_tree.print_tree())
