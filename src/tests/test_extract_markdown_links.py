import unittest

from functions.extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_not_extract_images(self):
        matches = extract_markdown_links(
            "This is text with an ![link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([], matches)

    def test_not_extract_wrong_markdown(self):
        matches = extract_markdown_links("This is text with an [alt [text]](url)")
        self.assertEqual([], matches)
