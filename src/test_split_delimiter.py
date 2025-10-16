import unittest
from textnode import *
from split_delimiter import *


class TestSplitDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_result = [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" word", TextType.TEXT),
                    ]
        self.assertEqual(new_nodes, test_result)

    def test_multiple_bold(self):
        node  = TextNode("This is text with a **BOLD** word", TextType.TEXT)
        node2 = TextNode("I AM **YELLING** LOUDLY", TextType.TEXT)
        new_nodes   = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        test_result = [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("BOLD", TextType.BOLD),
                        TextNode(" word", TextType.TEXT),
                        TextNode("I AM ", TextType.TEXT),
                        TextNode("YELLING", TextType.BOLD),
                        TextNode(" LOUDLY", TextType.TEXT),
                    ]
        self.assertEqual(new_nodes, test_result)



if __name__ == "__main__":
    unittest.main()