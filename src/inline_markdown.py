from textnode import TextNode, TextType
import re
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            nodes = old_node.text.split(delimiter)
            if len(nodes) > 1 and len(nodes) % 2 == 0:
                raise Exception("invalid markdown, unmatched delimiter")
            for i in range(len(nodes)):
                if i % 2 != 0:
                    new_nodes.append(TextNode(nodes[i], text_type))
                else:
                    new_nodes.append(TextNode(nodes[i], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
