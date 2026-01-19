import unittest

from enums import TextType
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        node2 = TextNode("This is an italic text", TextType.ITALIC)

        self.assertNotEqual(node, node2)

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev/")

        self.assertHasAttr(node, "url")
