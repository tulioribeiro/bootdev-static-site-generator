import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "There's no place like home!",
            {"href": "http://127.0.0.1/", "target": "_self", "id": "the-one"},
        )

        self.assertEqual(
            node.to_html(),
            '<a href="http://127.0.0.1/" target="_self" id="the-one">There\'s no place like home!</a>',
        )

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "AAAAAAAHHHH!")

        self.assertEqual(node.to_html(), "<b>AAAAAAAHHHH!</b>")
