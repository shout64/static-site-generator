import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node  = TextNode("This is a test node", TextType.ITALIC)
        node2 = TextNode("This is a test node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_urls(self):
        node  = TextNode("Yet another test", TextType.LINK, url="http://boot.dev")
        node2 = TextNode("Yet another test", TextType.LINK)
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()