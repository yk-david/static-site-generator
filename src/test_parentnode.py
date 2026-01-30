import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode('span', 'child')
        parent_node = ParentNode('div', [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span>child</span></div>')
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode('b', 'grandchild')
        child_node = ParentNode('span', [grandchild_node])
        parent_node = ParentNode('div', [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            '<div><span><b>grandchild</b></span></div>'
        )
    
    def test_to_html_with_two_children(self):
        child_node1 = LeafNode('span', 'child1')
        child_node2 = LeafNode('a', 'child2', {"href": "https://www.freecodecamp.org"})
        parent_node = ParentNode('section', [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(), 
            "<section><span>child1</span><a href='https://www.freecodecamp.org'>child2</a></section>"
        )
    
    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode('span', 'great grandchild')
        grandchild_node = ParentNode('p', [great_grandchild_node])
        child_node1 = ParentNode('div', [grandchild_node])
        child_node2 = LeafNode('h2', 'Is it working?')
        parent_node = ParentNode('div', [child_node1, child_node2], {'class': 'container'})
        self.assertEqual(
            parent_node.to_html(), 
            "<div class='container'><div><p><span>great grandchild</span></p></div><h2>Is it working?</h2></div>"
        )