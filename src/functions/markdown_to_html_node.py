from functions.block_to_html_node import block_to_html_node
from functions.markdown_to_blocks import markdown_to_blocks
from htmlnode import HTMLNode
from parentnode import ParentNode


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    block_nodes: list[HTMLNode] = []

    for block in blocks:
        node = block_to_html_node(block)
        block_nodes.append(node)

    return ParentNode("div", block_nodes)
