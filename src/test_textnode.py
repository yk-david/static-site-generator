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


if __name__ == '__main__':
    unittest.main()
