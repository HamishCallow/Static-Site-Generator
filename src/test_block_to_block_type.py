import unittest

from markdown_blocks import BlockType, block_to_block_type

class TestBlocksToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "###### This is a heading"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, output)

    def test_too_long_heading(self):
        block = "####### This is not a heading"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, output)

    def test_code1(self):
        block = "```code\n more code```"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, output)

    def test_code2(self):
        block = "```not code"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, output)

    def test_quote1(self):
        block = "> a\n> b\n> c"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, output)

    def test_quote2(self):
        block = " a\n> b\n- c"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, output)

    def test_ulist1(self):
        block = "- a\n- b\n- c"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.ULIST, output)
    
    def test_ulist2(self):
        block = "- a\n- b\n-c"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, output)

    def test_olist1(self):
        block = "1. a\n2. b\n3. c"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.OLIST, output)

    def test_olist2(self):
        block = "1. a\n3. b\n2. c"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, output)

    def test_paragraph(self):
        block = "this is a paragraph"
        output = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, output)


if __name__ == "__main__":
    unittest.main()
