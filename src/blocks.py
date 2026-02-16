import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'
    

def markdown_to_blocks(markdown):
    blocks = map(lambda x: x.strip(), markdown.split('\n\n'))

    return list(blocks)


def block_to_block_type(markdown_block):
    if markdown_block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    elif markdown_block.startswith('```\n') and markdown_block.endswith('```'):
        return BlockType.CODE
    elif markdown_block.startswith('>'):
        return BlockType.QUOTE
    elif markdown_block.startswith('- '):
        return BlockType.UNORDERED_LIST
    elif int(markdown_block.split(' ', 1)[0][0]) > 0 and markdown_block.split(' ', 1)[0][-1] == '.':
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

