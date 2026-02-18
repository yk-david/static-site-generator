from blocks import *
from htmlnode import *
from textnode import *


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            lines = ' '.join(block.split(' ', 1)[-1].split('\n'))
            block_nodes.append(ParentNode(f'h{get_heading_size(block)}', text_to_children(lines)))
        if block_type == BlockType.QUOTE:
            lines = block.split('\n')
            lines = ' '.join(line.split('>', 1)[-1].lstrip() for line in lines)
            block_nodes.append(ParentNode('blockquote', text_to_children(lines)))
        if block_type == BlockType.PARAGRAPH:
            lines = ' '.join(block.split('\n'))
            block_nodes.append(ParentNode('p', text_to_children(lines)))
        if block_type == BlockType.CODE:
            code_text = ''
            if block.startswith('```\n') and block.endswith('```'):
                code_text = block[4:-3] 
            block_nodes.append(ParentNode('pre', [LeafNode('code', code_text)]))
        if block_type == BlockType.UNORDERED_LIST:
            lines = block.split('\n')
            lines = (line.split(' ', 1)[-1] for line in lines if line.startswith(('- ', '* ')))
            children = []
            for line in lines:
                children.append(ParentNode('li', text_to_children(line)))
            block_nodes.append(ParentNode('ul', children))
        if block_type == BlockType.ORDERED_LIST:
            lines = block.split('\n')
            children = []
            for line in lines:
                children.append(ParentNode('li', text_to_children(line.split(' ', 1)[-1])))
            block_nodes.append(ParentNode('ol', children))

    return ParentNode('div', block_nodes)


def get_heading_size(heading_block):
    return heading_block.split(' ', 1)[0].count('#')


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    
    return [text_node_to_html_node(node) for node in text_nodes]