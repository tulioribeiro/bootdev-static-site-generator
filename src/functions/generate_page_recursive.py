import os

from functions.extract_title import extract_title
from functions.markdown_to_html_node import markdown_to_html_node


def generate_page_recursive(from_path: str, template_path: str, dest_path: str):
    # print(f"Generating page from {from_path} to {dest_path}")

    if os.path.isfile(from_path):
        markdown_file = open(from_path, "r")
        markdown_text = markdown_file.read()
        markdown_file.close()

        template_file = open(template_path, "r")
        template_text = template_file.read()
        template_file.close()

        markdown_to_html = markdown_to_html_node(markdown_text).to_html()
        title = extract_title(markdown_text)

        final_html = template_text.replace("{{ Title }}", title).replace(
            "{{ Content }}", markdown_to_html
        )

        parent = os.path.dirname(dest_path)

        if parent and not os.path.exists(parent):
            os.mkdir(parent)

        if not os.path.exists(dest_path):
            os.mkdir(dest_path)

        with open(os.path.join(dest_path, "index.html"), "w") as f:
            _ = f.write(final_html)
    else:
        files = os.listdir(from_path)

        for file in files:
            source_path = os.path.join(from_path, file)
            destination_path = os.path.join(dest_path, file)

            if os.path.isdir(source_path):
                generate_page_recursive(source_path, template_path, destination_path)
            else:
                generate_page_recursive(source_path, template_path, dest_path)
