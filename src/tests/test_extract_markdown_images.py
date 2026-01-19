import unittest

from functions.extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_not_extract_links(self):
        matches = extract_markdown_images(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([], matches)

    def test_not_extract_wrong_markdown(self):
        matches = extract_markdown_images("This is text with an ![alt [text]](url)")
        self.assertEqual([], matches)
