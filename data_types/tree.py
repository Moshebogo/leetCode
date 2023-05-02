class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.root = None



    def search(self, value):
        curr_node = self.root
        if curr_node.value == value:
            return True
        else:
            curr_val = curr_node.value


