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

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_images_tuples = extract_markdown_images(node.text)
        if markdown_images_tuples == []:
            new_nodes.append(node)
        else:
            current_text = node.text
            for image in markdown_images_tuples:
                sections = current_text.split(f'![{image[0]}]({image[1]})', 1)
                if sections[0] != '':
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                current_text = sections[1]
            if current_text != '':
                new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_links_tuples = extract_markdown_links(node.text)
        if markdown_links_tuples == []:
            new_nodes.append(node)
        else:
            current_text = node.text
            for link in markdown_links_tuples:
                sections = current_text.split(f'[{link[0]}]({link[1]})', 1)
                if sections[0] != '':
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                current_text = sections[1]
            if current_text != '':
                new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_image(split_nodes_link([node]))
    for node in new_nodes:
        if node.text_type == TextType.TEXT:
            if '**' in node.text:
                new_nodes = split_nodes_delimiter(
                    new_nodes, '**', TextType.BOLD)
            if '_' in node.text:
                new_nodes = split_nodes_delimiter(
                    new_nodes, '_', TextType.ITALIC)
            if '`' in node.text:
                new_nodes = split_nodes_delimiter(
                    new_nodes, '`', TextType.CODE)

    return new_nodes


# print(text_to_textnodes(
#     'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'))


# [TextNode(This is , TextType.TEXT, None),
# TextNode(text, TextType.BOLD, None),
# TextNode( with an , TextType.TEXT, None),
# TextNode(italic, TextType.ITALIC, None),
# TextNode( word and a , TextType.TEXT, None),
# TextNode(code block, TextType.CODE, None),
# TextNode( and an , TextType.TEXT, None),
# TextNode(obi wan image, TextType.IMAGE, https://i.imgur.com/fJRm4Vk.jpeg),
# TextNode( and a , TextType.TEXT, None),
# TextNode(link, TextType.LINK, https://boot.dev)]
