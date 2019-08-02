class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = Node(data)

    def palindrome(self):
        stack = []
        curr_node =  self.head
        while curr_node:
            stack.append(curr_node.data)
            curr_node = curr_node.next
        temp = self.head
        x = len(stack)-1
        while x >=  0:
            if  stack[x] != temp.data:
                return False
                break
            temp = temp.next
            x -= 1
        return True

l1 =  linkedlist()
l1.insert("a")
l1.insert("a")
l1.insert("o")
l1.insert("a")
l1.insert("a")
l1.insert("b")
# l1.display()
print(l1.palindrome())
