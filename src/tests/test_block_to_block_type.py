import unittest

from enums import BlockType
from functions.block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_simple_paragraph(self):
        self.assertEqual(
            block_to_block_type("Just a simple string"), BlockType.PARAGRAPH
        )

    def test_heading_1(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_heading_2(self):
        self.assertEqual(block_to_block_type("## Heading"), BlockType.HEADING)

    def test_heading_3(self):
        self.assertEqual(block_to_block_type("### Heading"), BlockType.HEADING)

    def test_heading_4(self):
        self.assertEqual(block_to_block_type("#### Heading"), BlockType.HEADING)

    def test_heading_5(self):
        self.assertEqual(block_to_block_type("##### Heading"), BlockType.HEADING)

    def test_heading_6(self):
        self.assertEqual(block_to_block_type("###### Heading"), BlockType.HEADING)

    def test_not_heading(self):
        self.assertNotEqual(block_to_block_type("##Not Heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\nprint('hi')\n```"), BlockType.CODE)

    def test_not_code(self):
        self.assertNotEqual(block_to_block_type("``````"), BlockType.CODE)

    def test_not_code_2(self):
        self.assertNotEqual(block_to_block_type("```\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> this is a simple quote"), BlockType.QUOTE
        )

    def test_multiline_quote(self):
        self.assertEqual(
            block_to_block_type("> first line\n> second line"), BlockType.QUOTE
        )

    def test_not_quote(self):
        self.assertNotEqual(
            block_to_block_type(">first line\n> second line"), BlockType.QUOTE
        )

    def test_unordered_list(self):
        self.assertEqual(
            block_to_block_type("- this is a line\n- this is another line"),
            BlockType.UNORDERED_LIST,
        )

    def test_unordered_list_2(self):
        self.assertEqual(
            block_to_block_type("- this is just a simple list with one item"),
            BlockType.UNORDERED_LIST,
        )

    def test_not_unordered_list(self):
        self.assertNotEqual(
            block_to_block_type("-this is just a simple list with one item"),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. first item\n2. second item"), BlockType.ORDERED_LIST
        )

    def test_not_ordered_list(self):
        self.assertNotEqual(
            block_to_block_type("1.first item\n2. second item"), BlockType.ORDERED_LIST
        )

    def test_not_ordered_list_2(self):
        self.assertNotEqual(
            block_to_block_type("1. first item\n3. second item"), BlockType.ORDERED_LIST
        )
