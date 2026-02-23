from blocks import markdown_to_blocks


def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    title = list(filter(lambda x: x.startswith('# '), md_blocks))
    if not title:
        raise Exception('no title found')
    return title[0].strip[1:]    