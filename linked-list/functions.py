# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 06:57:25 2023

@author: Tulayev Izzat
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            # if temp.data==None:
            #     temp = temp.next
            #     continue
            print(temp.data)
            temp = temp.next
    def push(self, newnode):
        newnode = Node(newnode)
        newnode.next = self.head
        self.head = newnode
    def insertAfter(self, prev_node, new_node):
        if prev_node is None:
            print("Tugun mavjud emas")
            return 
        new_node = Node(new_node)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def deleteNode(self, key):
        temp = self.head # Dushanba
        if temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key: # True
                break
            prev = temp # Seshanba
            temp = temp.next # Chorshanba
        if temp==None:
            return
        prev.next = temp.next 
        temp = None
            