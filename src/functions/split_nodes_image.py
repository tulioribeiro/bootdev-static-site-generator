from enums import TextType
from functions.extract_markdown_images import extract_markdown_images
from textnode import TextNode


def split_nodes_image(old_nodes: list[TextNode]):
    if not old_nodes:
        return old_nodes

    if not any(node.text_type == TextType.TEXT for node in old_nodes):
        return old_nodes

    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if not node.text:
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_markdown = extract_markdown_images(node.text)

        if not extracted_markdown:
            new_nodes.append(node)
            continue

        current_text = node.text
        for alt, url in extracted_markdown:
            start, end = current_text.split(f"![{alt}]({url})", 1)
            if start:
                new_nodes.append(TextNode(start, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.TEXT, url))

            current_text = end

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes
