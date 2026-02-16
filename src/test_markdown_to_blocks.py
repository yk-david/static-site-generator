import unittest
from blocks import *


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


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_heading(self):
        markdown_block = '# This lesson is about Block Types'
        type = block_to_block_type(markdown_block)
        self.assertEqual(type, BlockType.HEADING)
    
    def test_block_to_code(self):
        markdown_block = '```\nfor (let i = 0; i < 8; i++) { console.log(i) }; ```'
        type = block_to_block_type(markdown_block)
        self.assertEqual(type, BlockType.CODE)
    
    def test_block_to_quote(self):
        markdown_block = '> He said like this'
        type = block_to_block_type(markdown_block)
        self.assertEqual(type, BlockType.QUOTE)

    def test_block_to_unordered_list(self):
        markdown_block = '- item1'
        type = block_to_block_type(markdown_block)
        self.assertEqual(type, BlockType.UNORDERED_LIST)
    
    def test_block_to_ordered_list(self):
        markdown_block = '3. You should buy...'
        type = block_to_block_type(markdown_block)
        self.assertEqual(type, BlockType.ORDERED_LIST)