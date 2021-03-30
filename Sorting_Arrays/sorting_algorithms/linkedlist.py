from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def prepend_node(self, data):
        prepend_node = Node(data)
        prepend_node.next = self.head
        self.head = prepend_node

    def find_data(self, list_entry,entry):
        temporary_node = list_entry.head
        while True:
            if temporary_node.data == entry:
                print(f'{temporary_node} contains the data that you were looking for: {entry}')
                return False
            else:
                temporary_node = temporary_node.next
