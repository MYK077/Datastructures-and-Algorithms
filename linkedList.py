class Node():
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head =  None

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
        elif self.head.next != None:
            curr_node = self.head.next
            while curr_node.next != None:
                prev_node = curr_node
                curr_node = curr_node.next
            curr_node.next = Node(data)
        else:
            self.head.next = Node(data)

    def display(self):
        emptyList = []
        node = self.head
        while node != None:
            emptyList.append(node.data)
            node = node.next
        print(emptyList)

    def displaySize(self):
        size = 0
        node = self.head
        while node != None:
            size = size + 1
            node = node.next
        print(size)

    # remove by data input
    def removedByParticular(self, value):
        if value == self.head:
            self.head = self.head.next
        


    # insert at particular
    def insertParticularItem(self, value):
        return

    # delete with data input


l1 = LinkedList()

l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)

l1.displaySize()

l1.removedByParticular(1)

l1.display()
