## Linked List DEMO

class Node():
    def __init__(self, data):
        self.data = data 
        self.pointer = None
        # By default the pointer will point to None.
        # We will asign a pointer when we come to "link" our nodes
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, item):
        """Appends a node to the end of the linked list."""
        if not isinstance(item, Node):
            item = ListNode(item)

        if self.head is None:
            self.head = item            
        else:
            self.tail.pointer = item
        self.tail = item
    
    def getLength(self):
        """Returns the length of the linked list."""
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.pointer
        return count
    
    def printList(self):
        """Cycles through each node in the linked lists and prints each
        one in sequence"""
        print("CODE ME")
    
    def searchList(self, elmnt, all_nodes=False):
        """Searches for <elmnt> in the linked list and returns the node 
        number where the element is found or returns False if it fails
        to find."""
        print("CODE ME!")
                
    def deleteItem(self, pos):
        """Removes the item at specified position from the linked list"""
        print("CODE ME!")

    def insert(self, pos):
        """Inserts a new element into position pos in the list"""
        print("CODE ME!")
    
    def reverse(self):
        """Reverses the linking order of the list structure"""
        print("CODE ME! - This is harder!")
    
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

example = LinkedList()

example.addNode(a)
example.addNode(b)
example.addNode(c)
example.addNode(d)
example.printList()
