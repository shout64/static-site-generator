from inline_markdown import *
from textnode import *
from main import *
import unittest


class TestExtractTitle(unittest.TestCase):
    def test_tolkien(self):
        title = extract_title("content/index.md")
        test  = "Tolkien Fan Club"
        self.assertEqual(title, test)