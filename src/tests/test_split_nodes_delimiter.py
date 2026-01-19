import unittest

from enums import TextType
from functions.split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_node_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_single_node_with_bold(self):
        node = TextNode("This is text with a **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold word", TextType.BOLD),
            ],
        )

    def test_single_node_with_italic(self):
        node = TextNode("This is text with a _italic word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic word", TextType.ITALIC),
            ],
        )

    def test_complete_delimited(self):
        node = TextNode("**This is a full bold text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a full bold text", TextType.BOLD),
            ],
        )

    def test_two_nodes_together(self):
        nodes = split_nodes_delimiter(
            [
                TextNode("Just a **simple** string", TextType.TEXT),
                TextNode("Another **simple** string", TextType.TEXT),
            ],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(
            nodes,
            [
                TextNode("Just a ", TextType.TEXT),
                TextNode("simple", TextType.BOLD),
                TextNode(" string", TextType.TEXT),
                TextNode("Another ", TextType.TEXT),
                TextNode("simple", TextType.BOLD),
                TextNode(" string", TextType.TEXT),
            ],
        )

    def test_two_nodes_together_only_one_delimited(self):
        nodes = split_nodes_delimiter(
            [
                TextNode("Just a **simple** string", TextType.TEXT),
                TextNode("Another simple string", TextType.TEXT),
            ],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(
            nodes,
            [
                TextNode("Just a ", TextType.TEXT),
                TextNode("simple", TextType.BOLD),
                TextNode(" string", TextType.TEXT),
                TextNode("Another simple string", TextType.TEXT),
            ],
        )

    def test_two_nodes_together_without_delimiters(self):
        nodes = split_nodes_delimiter(
            [
                TextNode("Just a simple string", TextType.TEXT),
                TextNode("Another simple string", TextType.TEXT),
            ],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(
            nodes,
            [
                TextNode("Just a simple string", TextType.TEXT),
                TextNode("Another simple string", TextType.TEXT),
            ],
        )

    def test_invalid_markdown(self):
        with self.assertRaisesRegex(Exception, "Invalid markdown string"):
            _ = split_nodes_delimiter(
                [TextNode("An **invalid markdown string", TextType.TEXT)],
                "**",
                TextType.BOLD,
            )
