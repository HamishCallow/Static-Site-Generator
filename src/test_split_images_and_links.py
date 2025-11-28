import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_image, split_nodes_link

class TestSplitImagesAndLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("Just plain text, no images here.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_images_only_image(self):
        node = TextNode("![alt text](https://example.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")],
            new_nodes,
        )
    def test_split_images_start_and_end(self):
        node = TextNode(
            "![first](https://example.com/1.png) middle text ![second](https://example.com/2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://example.com/1.png"),
                TextNode(" middle text ", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "https://example.com/2.png"),
            ],
            new_nodes,
        )

    def test_split_images_leaves_non_text_nodes(self):
        img_node = TextNode("alt", TextType.IMAGE, "https://example.com/x.png")
        text_node = TextNode("Before ![alt](https://example.com/x.png)", TextType.TEXT)
        new_nodes = split_nodes_image([img_node, text_node])
        self.assertListEqual(
            [
                img_node,
                TextNode("Before ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "https://example.com/x.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode("Just plain text, no links here.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_only_link(self):
        node = TextNode("[alt text](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("alt text", TextType.LINK, "https://example.com")],
            new_nodes,
        )

    def test_split_links_start_and_end(self):
        node = TextNode(
            "[first](https://example.com/1) middle text [second](https://example.com/2)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "https://example.com/1"),
                TextNode(" middle text ", TextType.TEXT),
                TextNode("second", TextType.LINK, "https://example.com/2"),
            ],
            new_nodes,
        )

    def test_split_links_leaves_non_text_nodes(self):
        link_node = TextNode("alt", TextType.LINK, "https://example.com/x")
        text_node = TextNode("Before [alt](https://example.com/x)", TextType.TEXT)
        new_nodes = split_nodes_link([link_node, text_node])
        self.assertListEqual(
            [
                link_node,
                TextNode("Before ", TextType.TEXT),
                TextNode("alt", TextType.LINK, "https://example.com/x"),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()
