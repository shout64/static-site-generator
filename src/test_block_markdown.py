from block_markdown import *
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_type_head(self):
        head  = "# This is a heading"
        block = block_to_block_type(head)
        self.assertEqual(block, BlockType.HEADING)

        head_three  = "### This is a heading3"
        block_three = block_to_block_type(head_three)
        self.assertEqual(block_three, BlockType.HEADING)

    def test_block_to_type_par(self):
        par  = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
        block = block_to_block_type(par)
        self.assertEqual(block, BlockType.PARAGRAPH)

    def test_block_to_type_ulist(self):
        ulist = "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        block = block_to_block_type(ulist)
        self.assertEqual(block, BlockType.UNORDERED_LIST)

    def test_block_to_type_olist(self):
        olist = "1. Item number one\n2. Item number two"
        block = block_to_block_type(olist)
        self.assertEqual(block, BlockType.ORDERED_LIST)

    def test_block_to_type_code(self):
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        