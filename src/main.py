import os
import shutil
import sys

from functions.generate_page_recursive import generate_page_recursive


def main():
    base_path = sys.argv[1] + "/" if len(sys.argv) > 1 else "/"
    markdown_path = os.path.join("content")
    template_path = os.path.join("template.html")
    destination_path = os.path.join("docs")
    static_path = os.path.join("static")

    copy(static_path, destination_path)
    generate_page_recursive(markdown_path, template_path, destination_path, base_path)


def copy(source: str, destination: str):
    if not os.path.isdir(destination):
        os.mkdir(destination)

    for file in os.listdir(source):
        current_path = os.path.join(source, file)
        target_path = os.path.join(destination, file)

        if os.path.isfile(current_path):
            _ = shutil.copy(current_path, target_path)
        else:
            copy(current_path, target_path)


main()
