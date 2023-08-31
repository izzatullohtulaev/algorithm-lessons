from functions import Node, LinkedList
llist = LinkedList()


firstNode = Node("Jhon")
secondNode = Node("Ben")
thirdNode = Node("Matthew")

llist.insert_end(firstNode)
llist.insert_end(thirdNode)
llist.insert_at(secondNode, 1)
llist.print_list()
llist.remove_last()
llist.print_list()