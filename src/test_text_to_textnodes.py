import unittest

from textnode import TextType, TextNode
from inline_markdown import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_mixed_markdown(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_no_formating(self):
        nodes = text_to_textnodes("Just some plain text, no tricks here.")
        self.assertListEqual(
            [
               TextNode("Just some plain text, no tricks here.", TextType.TEXT), 
            ],
            nodes,
        )

    def test_one_formating(self):
        nodes = text_to_textnodes("Look, **bold** only.")
        self.assertListEqual(
            [
                TextNode("Look, ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" only.", TextType.TEXT),
            ],
            nodes,
        )

    def test_multiple_links_and_images(self):
        nodes = text_to_textnodes("Check this ![first image](https://example.com/first.png) and this [first link](https://example.com), then another ![second image](https://example.com/second.png) plus a [second link](https://example.org/docs).")
        self.assertListEqual(
            [
                TextNode("Check this ", TextType.TEXT),
                TextNode("first image", TextType.IMAGE, "https://example.com/first.png"),
                TextNode(" and this ", TextType.TEXT),
                TextNode("first link", TextType.LINK, "https://example.com"),
                TextNode(", then another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://example.com/second.png"),
                TextNode(" plus a ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org/docs"),
                TextNode(".", TextType.TEXT),
            ],
            nodes,
        )

    def test_punctuation(self):
        nodes = text_to_textnodes("Hello, **world**!")
        self.assertListEqual(
            [
                TextNode("Hello, ", TextType.TEXT),
                TextNode("world", TextType.BOLD),
                TextNode("!", TextType.TEXT),
            ],
            nodes,
        )

if __name__ == "__main__":
    unittest.main()
