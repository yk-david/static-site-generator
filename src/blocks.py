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


def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    elif block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    elif all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(int(line.split(' ', 1)[0]) > 0 and line.split(' ', 1)[-1] == '.' for line in lines):
        return BlockType.ORDERED_LIST

    # for line in lines:
    
    # for line in lines:
    #     if int(block.split(' ', 1)[0][0]) > 0 and block.split(' ', 1)[0][-1] == '.':
    #         return BlockType.ORDERED_LIST
    #     return BlockType.PARAGRAPH
    
    return BlockType.PARAGRAPH

        

