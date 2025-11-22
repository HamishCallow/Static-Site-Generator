import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_mult_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
    
    def test_no_props(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, "")
    
    def test_one_props(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"')

if __name__ == "__main__":
    unittest.main()
