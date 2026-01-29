import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag='<link>', props={'rel': 'stylesheet', 'href': './styles.css'})
        self.assertEqual(node.props_to_html(), " rel='stylesheet' href='./styles.css'")

    def test_values(self):
        node = HTMLNode('div', 'I wish I could')
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'I wish I could')

    def test_repr(self):
        node = HTMLNode(tag='p', value='my test', props={'class': 'my-text', 'id': 'my-paragraph'})
        self.assertEqual(repr(node), "HTMLNode(p, my test, children: None, {'class': 'my-text', 'id': 'my-paragraph'})")


if __name__ == '__main__':
    unittest.main()