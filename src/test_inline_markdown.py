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

class TestSplitLinkImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

class TestTextToTextNode(unittest.TestCase):
    def test_basic_case(self):
        input_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result     = text_to_textnodes(input_text)
        test_case  = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(result, test_case)


    def test_complex_text(self):
        input_text = "Here's [a link](https://sproutsocial.com/careers/open-positions/7279227/?gh_src=fe8bf1621us) to a _Software Engineering_ job opportunity!"
        result     = text_to_textnodes(input_text)
        test_case  = [
            TextNode("Here's ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "https://sproutsocial.com/careers/open-positions/7279227/?gh_src=fe8bf1621us"),
            TextNode(" to a ", TextType.TEXT),
            TextNode("Software Engineering", TextType.ITALIC),
            TextNode(" job opportunity!", TextType.TEXT)
        ]
        self.assertListEqual(result, test_case)

if __name__ == "__main__":
    unittest.main()