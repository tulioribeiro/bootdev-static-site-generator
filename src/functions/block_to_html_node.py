import re

from enums import BlockType, TextType
from functions.block_to_block_type import block_to_block_type
from functions.split_nodes_delimiter import split_nodes_delimiter
from functions.split_nodes_image import split_nodes_image
from functions.split_nodes_link import split_nodes_link
from functions.text_node_to_html_node import text_node_to_html_node
from functions.text_to_textnodes import text_to_textnodes
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode


def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    match block_type:
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return olist_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return ulist_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case _:  # BlockType.PARAGRAPH
            return paragraph_to_html_node(block)


def code_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    lines = lines[1:-1]
    lines = [line.strip() for line in lines]

    text_node = TextNode("\n".join(lines), TextType.CODE)

    return ParentNode("pre", [text_node_to_html_node(text_node)])


def heading_to_html_node(block: str) -> HTMLNode:
    heading = len(block) - len(block.lstrip("#"))

    text = block.lstrip("#").strip()

    return ParentNode(f"h{heading}", text_to_children(text))


def olist_to_html_node(block: str) -> HTMLNode:
    items: list[ParentNode] = []
    for line in block.split("\n"):
        striped_line = line.strip()
        striped_line = re.sub(r"\d\.\s", "", striped_line)
        items.append(ParentNode("li", text_to_children(striped_line)))

    return ParentNode("ol", items)


def ulist_to_html_node(block: str) -> HTMLNode:
    items: list[ParentNode] = []
    for line in block.split("\n"):
        striped_line = line.strip()
        striped_line = striped_line[2:]
        items.append(ParentNode("li", text_to_children(striped_line)))
    return ParentNode("ul", items)


def quote_to_html_node(block: str) -> HTMLNode:
    striped_block = [line.strip("> ") for line in block.split("\n")]
    return ParentNode("blockquote", text_to_children(" ".join(striped_block)))


def paragraph_to_html_node(block: str) -> HTMLNode:
    striped_block = [line.strip() for line in block.split("\n")]
    return ParentNode("p", text_to_children(" ".join(striped_block)))


def text_to_children(block: str) -> list[HTMLNode]:
    nodes = text_to_textnodes(block)

    return [text_node_to_html_node(node) for node in nodes]
