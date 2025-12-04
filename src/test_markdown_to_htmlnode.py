import unittest

from markdown_blocks import markdown_to_html_node

class TestBlocksToBlockType(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_all(self):
        md = """
# Heading 1

This is a _paragraph_ with **bold** text.

> A quoted line
> with `code` inside

- First _item_
- Second **item**

1. Number one
2. Number two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><p>This is a <i>paragraph</i> with <b>bold</b> text.</p><blockquote>A quoted line\nwith <code>code</code> inside</blockquote><ul><li>First <i>item</i></li><li>Second <b>item</b></li></ul><ol><li>Number one</li><li>Number two</li></ol></div>"
            )

if __name__ == "__main__":
    unittest.main()
