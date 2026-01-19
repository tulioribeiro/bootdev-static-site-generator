import unittest

from enums import TextType
from functions.text_to_textnodes import text_to_textnodes
from textnode import TextNode


class TestTextToTextNodes(unittest.TestCase):
    def test_full_markdown(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_markdown_at_the_beginning(self):
        nodes = text_to_textnodes(
            "**This text** with an _italic_ word and a `code block`!"
        )
        self.assertListEqual(
            [
                TextNode("This text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode("!", TextType.TEXT),
            ],
            nodes,
        )

    def test_full_bold(self):
        nodes = text_to_textnodes("**This text is just a bold text and nothing more**")
        self.assertListEqual(
            [
                TextNode(
                    "This text is just a bold text and nothing more", TextType.BOLD
                ),
            ],
            nodes,
        )
