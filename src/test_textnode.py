import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode('This is a link node', TextType.LINK, 'https://www.naver.com')
        node2 = TextNode('This is a link node', TextType.LINK, 'https://www.google.com')
        self.assertNotEqual(node, node2)

    def test_not_none(self):
        node = TextNode('This is a link node', TextType.LINK, 'https://www.naver.com')
        node2 = TextNode('This is a link node', TextType.LINK, 'https://www.google.com') 
        self.assertIsNotNone(node)
        self.assertIsNotNone(node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, 'This is a text node')
    
    def test_image(self):
        node = TextNode('This is an image', TextType.IMAGE, 'https://www.coupang.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {'src': 'https://www.coupang.com', 'alt': 'This is an image'})

    def test_link(self):
        node = TextNode('some link here', TextType.LINK, 'https://www.coursera.org')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {'href': 'https://www.coursera.org'})


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(new_node, [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(" word", TextType.TEXT)
        ])
    
    def test_italic(self):
        node = TextNode('_This challenge_ was particularly hard to solve...', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertEqual(new_node, [
            TextNode('', TextType.TEXT), 
            TextNode('This challenge', TextType.ITALIC), 
            TextNode(' was particularly hard to solve...', TextType.TEXT)
        ])

    def test_bold(self):
        node = TextNode('Ok, now **bold** to test!', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertEqual(new_node, [
            TextNode('Ok, now ', TextType.TEXT), 
            TextNode('bold', TextType.BOLD), 
            TextNode(' to test!', TextType.TEXT)
        ])
    
    def test_bold_and_italic(self):
        node = TextNode('The **HARDEST** challenge _ever_...', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '**', TextType.BOLD)
        new_node = split_nodes_delimiter(new_node, '_', TextType.ITALIC)
        self.assertEqual(new_node, [
            TextNode('The ', TextType.TEXT), 
            TextNode('HARDEST', TextType.BOLD), 
            TextNode(' challenge ', TextType.TEXT), 
            TextNode('ever', TextType.ITALIC), 
            TextNode('...', TextType.TEXT)
        ])



if __name__ == '__main__':
    unittest.main()
