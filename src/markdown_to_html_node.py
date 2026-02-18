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
            lines = block.split('\n')
            paragraph = ' '.join(lines)
            block_nodes.append(ParentNode('p', text_to_children(paragraph)))
        if block_type == BlockType.CODE:
            if not block.startswith('```') or not block.endswith('```'):
                raise ValueError('invalid code block')
            code_text = block[4:-3] # it starts at 4 because code blocks comes with \n (line break) 
            raw_code_text_node = TextNode(code_text, TextType.TEXT)
            child_html_node = text_node_to_html_node(raw_code_text_node)
            block_nodes.append(ParentNode('pre', [ParentNode('code', [child_html_node])]))
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
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
    # return [text_node_to_html_node(node) for node in text_nodes]