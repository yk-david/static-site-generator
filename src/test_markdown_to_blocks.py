import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_example(self):
        md = '''
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
'''
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, [
            'This is **bolded** paragraph', 
            'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line', 
            '- This is a list\n- with items'
        ])


    def test_markdown_to_blocks_first(self):
        md = '''
# Split Blocks

Our _grug-brain_ static site generator only cares about **two** things:

* Inline markdown
* Block markdown
'''
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, [
            '# Split Blocks', 
            'Our _grug-brain_ static site generator only cares about **two** things:', 
            '* Inline markdown\n* Block markdown'
        ])

    
    def test_markdown_to_blocks_second(self):
        md = '''
# Title

First paragraph line one
line two of same paragraph

> This is a quote
> still the same quote block

1. First item
2. Second item
3. Third item
'''
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, [
            '# Title', 
            'First paragraph line one\nline two of same paragraph', 
            '> This is a quote\n> still the same quote block', 
            '1. First item\n2. Second item\n3. Third item'
        ])