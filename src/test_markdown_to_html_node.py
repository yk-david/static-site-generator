import unittest
from markdown_to_html_node import *


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    

    def test_headings_paragraphs(self):
        md = '''
# The Great Bear

This is a paragraph about
a very large bear that
lives in the woods.

## Subheading here
'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>The Great Bear</h1><p>This is a paragraph about a very large bear that lives in the woods.</p><h2>Subheading here</h2></div>' 
        )
    

    def test_inline_styles_list(self):
        md = '''
- Item with **bold**
- Item with `inline code`
- Regular item
'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            '<div><ul><li>Item with <b>bold</b></li><li>Item with <code>inline code</code></li><li>Regular item</li></ul></div>'
        )


    def test_blociquotes_and_nested_content(self):
        md = '''
> This is a quote
> that spans two lines
> with _italics_ included.
'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            '<div><blockquote>This is a quote that spans two lines with <i>italics</i> included.</blockquote></div>'
        )
    

    def test_ol(self):
        md = '''
1. First item
2. Second item
3. Third item
'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            '<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>'
        )