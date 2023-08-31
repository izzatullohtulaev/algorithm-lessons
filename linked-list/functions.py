class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def get_length(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
    def insert_end(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = newNode
                break
            currentNode = currentNode.next
    def print_list(self):
        if self.head is None:
            print("Current List is empty!")
            return
        currentNode = self.head
        while True:
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode == None:
                break
    def insert_head(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        tempNode = self.head
        self.head=newNode
        self.head.next = tempNode
    def insert_between(self, newNode, first, second):
        first.next = newNode
        newNode.next = second
    def insert_at(self, newNode, position):
        if position == 0:
            self.insert_head(newNode)
            return
        if position < 0 or position>self.get_length():
            print("Invalid position!")
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                prevNode.next = newNode
                newNode.next = currentNode
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
    def remove_last(self):
        currentNode = self.head
        index = 0
        while True:
            if index == self.get_length()-1:
                tempNode = currentNode
                del currentNode.next
                tempNode.next = None
                break
            currentNode = currentNode.next
            index += 1