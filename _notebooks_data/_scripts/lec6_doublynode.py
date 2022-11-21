class DoublyNode:

    def __init__(self, data, nextnode, prevnode):
        self.data = data
        self.next = nextnode
        self.prev = prevnode


class DoublyLinkedList:

    def __init__(self, sequence):

        nodes_list = []
        for i, elem in enumerate(sequence):
            node = DoublyNode(elem, None, None)
            nodes_list.append(node)

        for i, node in enumerate(nodes_list):

            if i == 0:
                node.next = nodes_list[i + 1]
            elif i == len(nodes_list) - 1:
                node.prev = nodes_list[i - 1]
            else:
                node.next = nodes_list[i + 1]
                node.prev = nodes_list[i - 1]

        self.head = nodes_list[0]
        self.tail = nodes_list[-1]
        self.direction = True

        self._len = len(sequence)

    def __iter__(self):

        if self.direction:
            node = self.head
            while node is not None:
                yield node
                node = node.next
        else:
            node = self.tail
            while node is not None:
                yield node
                node = node.prev

    def __str__(self):
        res_row = ""
        for node in self:
            if node == self.head and self.direction:
                res_row += f"({node.data})"
            elif node == self.tail and not self.direction:
                res_row += f"({node.data})"
            else:
                res_row += f" -> ({node.data})"

        return res_row

    def __len__(self):
        return self._len