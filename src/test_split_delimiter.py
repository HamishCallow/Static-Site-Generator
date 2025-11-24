import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiters(self):
        node = TextNode("plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("plain text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_valid_pair(self):
        node = TextNode("This is `code` here", TextType.TEXT) 
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_invalid(self):
        node = TextNode("This is `code here", TextType.TEXT)
        with self.assertRaises(Exception) as ctx:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("invalid markdown, unmatched delimiter", str(ctx.exception))

    def test_bold_pair(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_pair(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_mixed_non_text_node(self):
        nodes = [
            TextNode("start **bold**", TextType.TEXT),
            TextNode("link", TextType.BOLD),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("start ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.TEXT),
            TextNode("link", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
