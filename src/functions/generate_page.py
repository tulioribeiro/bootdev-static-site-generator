import os

from functions.extract_title import extract_title
from functions.markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path, "r+")
    markdown_text = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r+")
    template_text = template_file.read()
    template_file.close()

    markdown_to_html = markdown_to_html_node(markdown_text).to_html()
    title = extract_title(markdown_text)

    final_html = template_text.replace("{{ Title }}", title).replace(
        "{{ Content }}", markdown_to_html
    )

    with open(os.path.join(dest_path, "index.html"), "w") as f:
        _ = f.seek(0)
        _ = f.write(final_html)
        f.close()
