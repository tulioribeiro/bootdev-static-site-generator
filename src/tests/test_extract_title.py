import unittest

from functions.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        markdown = """
        # Valid title markdown
        """

        title = extract_title(markdown)
        self.assertEqual(title, "Valid title markdown")

    def test_valid_title_2(self):
        markdown = """
        just a paragraph before

        # Valid title markdown after paragraph
        """

        title = extract_title(markdown)
        self.assertEqual(title, "Valid title markdown after paragraph")

    def test_invalid_markdown(self):
        with self.assertRaisesRegex(Exception, "No title found"):
            _ = extract_title("There's no title")
