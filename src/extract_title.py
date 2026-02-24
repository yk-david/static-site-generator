from blocks import markdown_to_blocks


def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    title = list(filter(lambda x: x.startswith('# '), md_blocks))
    if not title:
        raise Exception('no title found')
    if len(title) > 1:
        raise Exception('to many titles: you only can have one h1 title in html document')
    return title[0].strip()[1:]    