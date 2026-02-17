from blocks import *
from htmlnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            return HTMLNode(f'h{get_heading_size(block)}', block.split('.', 1)[-1])
        if block_type == BlockType.CODE:
            pass


def get_heading_size(heading_block):
    return heading_block.split(' ', 1).count('#')