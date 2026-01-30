import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'Hello, world!')
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')
    
    def test_leaf_to_html_a(self):
        node = LeafNode('a', 'You can click here!', props={'href': 'https://www.naver.com'})
        self.assertEqual(node.to_html(), "<a href='https://www.naver.com'>You can click here!</a>")

    def test_leaf_to_html_button(self):
        node = LeafNode('button', 'Get the deal!', props={'type': 'submit', 'id': 'submit-btn'})
        self.assertEqual(node.to_html(), "<button type='submit' id='submit-btn'>Get the deal!</button>")


if __name__ == '__main__':
    unittest.main()