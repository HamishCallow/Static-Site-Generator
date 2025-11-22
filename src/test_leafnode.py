import unittest

from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_p2(self):
        node = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<a>Hello, world!</a>")


if __name__ == "__main__":
    unittest.main()
