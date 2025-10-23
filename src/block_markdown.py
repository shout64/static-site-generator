from textnode import *
from htmlnode import *
from enum     import Enum

class BlockType(Enum):
    PARAGRAPH      = "paragraph"
    HEADING        = "heading"
    CODE           = "code"
    QUOTE          = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST   ="ordered_list"

def markdown_to_blocks(markdown):
    raw_blocks      = markdown.split("\n\n")
    stripped_blocks = [block.strip() for block in raw_blocks]
    output          = []
    for block in stripped_blocks:
        if block != "":
            output.append(block)
    return output

def block_to_block_type(block):
    lines = block.split("\n")

    if "# " in block[0:6]:
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    # parent = ParentNode()
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
