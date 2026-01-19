import unittest

from enums import TextType
from functions.text_node_to_html_node import text_node_to_html_node
from textnode import TextNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Text!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Text!")

    def test_italic(self):
        node = TextNode("Text!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Text!")

    def test_code(self):
        node = TextNode("Text!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Text!")

    def test_link(self):
        node = TextNode("Text!", TextType.LINK, "https://web.com/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Text!")
        self.assertEqual(html_node.props, {"href": "https://web.com/"})

    def test_link_without_url(self):
        with self.assertRaises(ValueError):
            _ = text_node_to_html_node(TextNode("Text!", TextType.LINK))

    def test_image(self):
        node = TextNode("Text!", TextType.IMAGE, "https://web.com/a.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "https://web.com/a.jpg", "alt": "Text!"}
        )

    def test_image_without_url(self):
        with self.assertRaises(ValueError):
            _ = text_node_to_html_node(TextNode("Text!", TextType.IMAGE))


if __name__ == "__main__":
    _ = unittest.main()
