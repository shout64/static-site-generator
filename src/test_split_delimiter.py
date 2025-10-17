import unittest
from textnode import *
from inline_markdown import *


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

class TestLinkExtraction(unittest.TestCase):
    def test_image_url_extract(self):
        text   = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test   = extract_markdown_images(text)
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(test, result)

    def test_link_url_extract(self):
        text   = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test   = extract_markdown_links(text)
        result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(test, result)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


if __name__ == "__main__":
    unittest.main()