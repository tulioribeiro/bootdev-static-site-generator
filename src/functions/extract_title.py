import re

from functions.markdown_to_blocks import markdown_to_blocks


def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if re.match(r"^# ", block):
            return block.replace("# ", "")

    raise Exception("No title found")
