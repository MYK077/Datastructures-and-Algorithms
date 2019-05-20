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

    # remove by index
    def removedAtParticularPosition(self, position):
        curr_node = self.head
        index = 1
        if position <= 0:
            print("position is negative or zero")
            return
        elif position == 1:
            self.head = curr_node.next
            return
        while True:
            prev_node = curr_node
            curr_node = curr_node.next
            if index == (position -1) :
                prev_node.next = curr_node.next
                return
            index+= 1


    # insert at particular
    def insertParticularItem(self, position ,value):
        node =  Node(value)
        curr_node = self.head
        index  = 1
        if position <= 0 :
            print("index is negative or zero")
        elif position == 1:
            self.head = curr_node.next
            return
        while True:
            prev_node =  curr_node
            curr_node = curr_node.next
            if index == (position-1):
                prev_node.next = node
                node.next = curr_node
                return
            index+=1



    # delete with data input
    def deleteWithDataInput(self,value):
        curr_node = self.head
        while True:
            root_node = curr_node
            curr_node = curr_node.next
            if value == root_node.data:
                self.head = curr_node
                return
            elif value == curr_node.data:
                root_node.next = curr_node.next
                return




l1 = LinkedList()

l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.insert(6)
l1.insert(7)
l1.insert(8)
l1.insert(9)
l1.insert(10)

l1.displaySize()

# l1.deleteWithDataInput(8)

l1.insertParticularItem(1,90)

# l1.removedAtParticularPosition(3)

l1.display()
