import unittest

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_reg_markdown(self):
        md ="# Hello world"
        output = extract_title(md)
        self.assertEqual(output, "Hello world")
    
    def test_whitespace(self):
        md ="#  Hello world "
        output = extract_title(md)
        self.assertEqual(output, "Hello world")

    def test_header(self):
        md = "Hello world"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_no_h1_header(self):
        md = "## Hello world"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_max_test(self):
        md = "## h2 header\n#  Hello world \n# second h1"
        output = extract_title(md)
        self.assertEqual(output, "Hello world")

if __name__ == "__main__":
    unittest.main()
