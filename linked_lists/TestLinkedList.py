import unittest
from LinkedList import Node

class TestLinkedList(unittest.TestCase):
    def test_node(self):
        new_node = Node(1)
        self.assertEqual(new_node, "Data: 1")

if __name__ == "__main__":
    unittest.main()