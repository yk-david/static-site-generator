def markdown_to_blocks(markdown):
    blocks = map(lambda x: x.strip(), markdown.split('\n\n'))

    return list(blocks)