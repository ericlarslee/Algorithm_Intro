from linkedlist import LinkedList


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.prepend_node(29)
    linked_list.find_data(linked_list, 29)

