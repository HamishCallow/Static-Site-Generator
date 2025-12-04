from enum import Enum
from htmlnode import ParentNode, text_node_to_html_node
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        clean_block = block.strip()
        if clean_block != "": 
            blocks.append(clean_block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    elif block.startswith(">"):
        lines = block.split("\n")    
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    elif block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    elif block.startswith("1. "):
        i = 1
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    
    else:
        return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    parent = ParentNode("div", children=[])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        blocktype = block_to_block_type(block) 
        if blocktype == BlockType.HEADING:
            children = []
            level = 0
            for c in block:
                if c == "#":
                    level += 1
                else:
                    break
            text = block[level + 1 :]
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                htmlnode = text_node_to_html_node(textnode)
                children.append(htmlnode)
            heading_node = ParentNode(f"h{level}", children=children)
            parent.children.append(heading_node)

        elif blocktype == BlockType.QUOTE:
            children = []
            lines = block.split("\n")
            cleaned_lines = [line[2:] for line in lines if line]
            text = "\n".join(cleaned_lines)
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                htmlnode = text_node_to_html_node(textnode)
                children.append(htmlnode)
            quote_node = ParentNode("blockquote", children=children)
            parent.children.append(quote_node)

        elif blocktype == BlockType.ULIST:
            ul_children = []
            lines = block.split("\n")
            cleaned_lines = [line[2:] for line in lines if line]
            for line in cleaned_lines:
                li_children = []
                textnodes = text_to_textnodes(line)
                for textnode in textnodes:
                    htmlnode = text_node_to_html_node(textnode)
                    li_children.append(htmlnode)
                li_node = ParentNode("li", children=li_children)
                ul_children.append(li_node)
            ul_node = ParentNode("ul", children=ul_children)
            parent.children.append(ul_node)

        elif blocktype == BlockType.OLIST:
            ol_children = []
            lines = block.split("\n")
            cleaned_lines = [line[3:] for line in lines if line]
            for line in cleaned_lines:
                li_children = []
                textnodes = text_to_textnodes(line)
                for textnode in textnodes:
                    htmlnode = text_node_to_html_node(textnode)
                    li_children.append(htmlnode)
                li_node = ParentNode("li", children=li_children)
                ol_children.append(li_node)
            ol_node = ParentNode("ol", children=ol_children)
            parent.children.append(ol_node)

        elif blocktype == BlockType.CODE:
            children = []
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            text = "\n".join(inner_lines) + "\n"
            textnode = TextNode(text, TextType.CODE)
            code_child = text_node_to_html_node(textnode)
            pre_node = ParentNode("pre", children=[code_child])
            parent.children.append(pre_node)

        else:
            children = []
            lines = block.split("\n")
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            text = " ".join(cleaned_lines)
            textnodes = text_to_textnodes(text)
            for textnode in textnodes:
                htmlnode = text_node_to_html_node(textnode)
                children.append(htmlnode)
            paragraph_node = ParentNode("p", children=children)
            parent.children.append(paragraph_node)

    return parent

