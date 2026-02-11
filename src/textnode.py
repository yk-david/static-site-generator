from enum import Enum
from htmlnode import LeafNode
from extract_markdown import *


class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode('b', text_node.text)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode('i', text_node.text)
        if text_node.text_type == TextType.CODE:
            return LeafNode('code', text_node.text)
        if text_node.text_type == TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        if text_node.text_type == TextType.IMAGE:
            return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
        
        raise ValueError(f'invalid text type: {text_node.text_type}')


def split_nodes_delimiter(old_nodes, delimiter, text_type):  
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        if node.text_type == TextType.TEXT:
            delimiter_pair_count = node.text.count(delimiter)

            if delimiter_pair_count % 2 != 0:
                raise Exception('invalid markdown')
            
            split_texts = node.text.split(delimiter)
            
            for i in range(0, len(split_texts)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_texts[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_texts[i], text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    # for node in old_nodes:



def split_nodes_link(old_nodes): # `old_nodes` is a list of single or multiple TextNode`
    
    if markdown_links_tuples is None:
        return [old_nodes]
    new_nodes = []

    for node in old_nodes:
        markdown_links_tuples = extract_markdown_links(node)
        if markdown_links_tuples is None:
            new_nodes.append(node)
        else:
            
    




# [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]