import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        sample_props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node         = HTMLNode(props=sample_props)
        node_result  = node.props_to_html()
        test_case    =  " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node_result, test_case)

    def test_HTMLNode_repr(self):
        node      = HTMLNode("<p>", "This is my test", None, None)
        node_repr = repr(node)
        test_case = "tag = <p>, value = This is my test, children = None, props = None"
        self.assertEqual(node_repr, test_case)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "THIS IS IMPORTANT")
        self.assertEqual(node.to_html(), "<b>THIS IS IMPORTANT</b>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "something.com", {"href": "homestarrunner.com"})
        self.assertEqual(node.to_html(), "<a href=\"homestarrunner.com\">something.com</a>")
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.children, None)

class TestParentNode(unittest.TestCase):
    def test_nested_leaf_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_no_children(self):
        parent = ParentNode("h1", None)
        # self.assertEqual(parent.to_html(), "ValueError: Node must have children")
        self.assertRaises(ValueError, parent.to_html)