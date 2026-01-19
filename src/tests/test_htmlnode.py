import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Just a link",
            None,
            {"href": "https://boot.dev", "target": "_blank"},
        )

        self.assertEqual(
            node.props_to_html(), ' href="https://boot.dev" target="_blank"'
        )

    def test_props_to_html2(self):
        node = HTMLNode(
            "p",
            "Just a paragraph",
            None,
            {"title": "batata", "class": "some classes here"},
        )

        self.assertEqual(
            node.props_to_html(), ' title="batata" class="some classes here"'
        )

    def test_props_to_html3(self):
        node = HTMLNode(
            "div",
            "Just a div",
            None,
            {"aria-hidden": "true"},
        )

        self.assertEqual(node.props_to_html(), ' aria-hidden="true"')
