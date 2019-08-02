class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head =  None

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = Node(data)


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
            self.head = node
            self.head.next = curr_node
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
# Remove the duplicate elements
    def removeDuplicates(self, linkedlist):
        prev_node =  self.head
        curr_node = prev_node.next
        keys = set([linkedlist])

        while curr_node:
            data = curr_node.data
            # if node.data is present in the keys then discard
            if data in keys:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
            # else add the data to the keys
            else:
                keys.add(data)
                prev_node = curr_node
                curr_node = curr_node.next

# Return Kth element from last element
    def kth_from_Last(self,k):
        listLength = 0
        position = k
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            listLength +=1

        if k > listLength or k < 0:
            print("the number entered is either negative of less than 0")
        temp = self.head
        for x in range(0, listLength-k):
                temp = temp.next
        return temp.data

# delete the mddle node from the list
    def delMiddleNode(self):
        listLength = 0
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            listLength += 1
        position = listLength // 2
        count = 0
        curr_node = self.head
        while count <= position:
            if count == position:
                prev_node.next = curr_node.next
                break
            prev_node = curr_node
            curr_node = curr_node.next

            count+=1







l1 = LinkedList()

l1.insert(1)
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.insert(6)
l1.insert(7)
l1.insert(7)
l1.insert(8)
l1.insert(8)
l1.insert(9)
l1.insert(10)

l1.displaySize()
l1.display()
#
# l1.deleteWithDataInput(8)
#
# l1.display()
#
# l1.insertParticularItem(1,90)
# l1.insertParticularItem(1,93)
# l1.insertParticularItem(5,90)
#
# l1.display()
#
# l1.removedAtParticularPosition(3)
#
# l1.display()
# print("#######################################")
# l1.removeDuplicates(l1)
# l1.display()

print("from Kth to last")

print(l1.kth_from_Last(6))

l1.delMiddleNode()
l1.display()
