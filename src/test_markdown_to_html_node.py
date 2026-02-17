import unittest
from markdown_to_html_node import *


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        md = '''
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, '<div><p>THis is <b>bolded</b> paragraph</p><p>text in a p</p><p>tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>')