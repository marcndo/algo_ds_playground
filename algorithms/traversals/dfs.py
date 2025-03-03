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



    def inorder(self,current_node,mylist):
      if current_node != None:
        self.inorder(current_node.left,mylist)
        mylist.append(current_node.val)
        self.inorder(current_node.right,mylist)
      return mylist
  
    def preorder(self,current_node,mylist):
      if current_node!=None:
        mylist.append(current_node.val)
        self.preorder(current_node.left,mylist)
        self.preorder(current_node.right,mylist)
      return mylist
    
    def postorder(self,current_node,mylist):
      if current_node.left:
        self.postorder(current_node.left,mylist)
      if current_node.right:
        self.postorder(current_node.right,mylist)
      mylist.append(current_node.val)
      return mylist