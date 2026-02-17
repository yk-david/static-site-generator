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
        block = '# This lesson is about Block Types'
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.HEADING)
    
    def test_block_to_code(self):
        block = '```\nfor (let i = 0; i < 8; i++) { console.log(i) }; ```'
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.CODE)
    
    def test_block_to_multiline_quote(self):
        block = ">First line of quote\n>Second line of quote\n>Third line"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.QUOTE)

    def test_block_to_fake_quote(self):
        block = ">This is a quote\nBut this line is not"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_block_to_multiline_ul(self):
        block = "- First item\n- Second item\n- Third item"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.UNORDERED_LIST)
    
    def test_block_to_fake_ul(self):
        block = "- First item\n- Second item\nThis line breaks it"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_to_multiline_ol(self):
        block = "1. First item\n2. Second item\n3. Third item"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.ORDERED_LIST)

