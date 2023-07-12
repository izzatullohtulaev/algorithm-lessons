# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 07:06:47 2023

@author: Tulayev Izzat
"""

from functions import Node, LinkedList
llist = LinkedList()

llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")
thursday = Node("Payshanba")
friday = Node("Juma")
saturday = Node("Shanba")


llist.head.next = tuesday
tuesday.next = wednesday
wednesday.next = thursday
thursday.next = friday
friday.next = saturday
llist.printList()
print()

# llist.insertAfter(llist.head.next, "Dushanba kechasi")
llist.deleteNode("Chorshanba")
llist.printList()