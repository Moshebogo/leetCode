# each Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value    

# the Linked List
class LinkedList:
    def __init__(self, node):
        self.head = node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(f'{current_node.value} -> ') 
            current_node = current_node.next   
    
    def add_to_back(self, node):
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node    

    def add_to_front(self, node):
        node.next = self.head
        self.head = node



if __name__ == '__main__':
    a  = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    LL = LinkedList(a)
    LL.add_to_back(b)
    LL.add_to_back(c)
    LL.add_to_front(d)
    LL.print_list()