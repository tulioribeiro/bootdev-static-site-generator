import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_parent_with_one_child(self):
        leaf = LeafNode("p", "This is a p.")
        parent = ParentNode("div", [leaf], {"title": "Batata"})

        self.assertEqual(
            parent.to_html(), '<div title="Batata"><p>This is a p.</p></div>'
        )

    def test_parent_with_two_children(self):
        leaf = LeafNode("p", "This is a p.")
        leaf2 = LeafNode("a", "This is a a.")
        parent = ParentNode("div", [leaf, leaf2])

        self.assertEqual(
            parent.to_html(), "<div><p>This is a p.</p><a>This is a a.</a></div>"
        )

    def test_parent_with_one_child_as_parent(self):
        leaf = LeafNode("p", "This is a p.")
        leaf2 = LeafNode("a", "This is a a.")

        inner_parent = ParentNode("div", [leaf, leaf2])
        sibling = LeafNode("div", "Just a sibling")

        parent = ParentNode("article", [inner_parent, sibling])

        self.assertEqual(
            parent.to_html(),
            "<article><div><p>This is a p.</p><a>This is a a.</a></div><div>Just a sibling</div></article>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
