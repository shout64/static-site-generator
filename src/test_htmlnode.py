import unittest
from htmlnode import HTMLNode

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