from enums import TextType
from leafnode import LeafNode
from textnode import TextNode


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("LINK nodes must have a url")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("IMAGE nodes must have a url")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            return LeafNode(None, text_node.text)
