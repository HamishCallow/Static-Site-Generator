import unittest

from htmlnode import LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_parentnode_with_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>child</span></div>',
        )

    def test_parentnode_raises_no_tag(self):
        child = LeafNode("span", "child")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parentnode_raises_no_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_with_text_and_tags(self):
        child1 = LeafNode(None, "Hello ")
        child2 = LeafNode("b", "world")
        parent = ParentNode("p", [child1, child2])
        self.assertEqual(parent.to_html(), "<p>Hello <b>world</b></p>")


if __name__ == "__main__":
    unittest.main()
