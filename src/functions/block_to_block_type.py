import re

from enums import BlockType


def block_to_block_type(markdown: str):
    if re.match(r"#{1,6} ", markdown):
        return BlockType.HEADING

    if is_code_block(markdown):
        return BlockType.CODE

    if all(line.strip().startswith(">") for line in markdown.split("\n")):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in markdown.split("\n")):
        return BlockType.UNORDERED_LIST

    if is_ordered_list_block(markdown):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def is_ordered_list_block(markdown: str) -> bool:
    lines = markdown.split("\n")

    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            return False

    return True


def is_code_block(markdown: str) -> bool:
    lines = markdown.strip().split("\n")

    if len(lines) < 3:
        return False

    if not lines[0].startswith("```"):
        return False

    if not lines[-1].strip().startswith("```"):
        return False

    return True
