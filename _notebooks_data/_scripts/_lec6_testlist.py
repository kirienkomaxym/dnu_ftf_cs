import unittest
from lec6_doublynode import DoublyNode, DoublyLinkedList

class TestDoublyLList(unittest.TestCase):

    def test_init(self):
        seq = "abcd"
        dl_list = DoublyLinkedList(seq)

        # values
        self.assertTrue(dl_list.head.data == "a")
        self.assertTrue(dl_list.tail.data == "d")
        self.assertTrue(dl_list.head.next.data == "b")
        self.assertTrue(dl_list.tail.prev.data == "c")

        # links
        self.assertIsInstance(dl_list.head, DoublyNode)
        self.assertIsInstance(dl_list.tail, DoublyNode)

        self.assertIsInstance(dl_list.head.prev, type(None))
        self.assertIsInstance(dl_list.tail.next, type(None))

        self.assertIsInstance(dl_list.head.next, DoublyNode)
        self.assertIsInstance(dl_list.tail.prev, DoublyNode)

        # et cetera et cetera
        # seq = [1, 2, 3, 4, 5]
        # seq = []

    def test_len(self):

        seq = [1, 2, 3, 4, 5]
        dl_list = DoublyLinkedList(seq)

        self.assertEqual(len(seq), len(dl_list))

    def test_str(self):

        seq = [1, 2, 3]
        dl_list = DoublyLinkedList(seq)

        # forward
        dl_list.direction = True
        expected_str = f"(1) -> (2) -> (3)"
        self.assertEqual(str(dl_list), expected_str)

        # inverse
        dl_list.direction = False
        expected_str = f"(3) -> (2) -> (1)"
        self.assertEqual(str(dl_list), expected_str)

    def test_iter(self):

        seq = ("hi", "there", "im", "a", "node")
        dl_list = DoublyLinkedList(seq)
        dl_list.direction = True

        for index, node in enumerate(dl_list):
            self.assertIsInstance(node, DoublyNode)
            self.assertEqual(node.data, seq[index])

        dl_list.direction = False
        seq = tuple(reversed(seq))

        for index, node in enumerate(dl_list):
            self.assertIsInstance(node, DoublyNode)
            self.assertEqual(node.data, seq[index])


if __name__ == '__main__':
    unittest.main()