import unittest
from extract_markdown import *


class TestMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            'Search on [Google](https://www.google.com)'
        )
        self.assertListEqual([('Google', 'https://www.google.com')], matches)
    
    def test_extract_markdown_icons(self):
        matches = extract_markdown_images(
            'This is a ![svg](https://someurl/icon.svg)'
        )
        self.assertListEqual([('svg', 'https://someurl/icon.svg')], matches)